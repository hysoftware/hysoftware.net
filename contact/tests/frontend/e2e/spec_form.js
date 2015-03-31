/*global describe, beforeEach, afterEach, it, expect, browser, element, by*/
(function (describe, beforeEach, afterEach, it, expect, browser, element, by) {
    "use strict";
    describe("Contact Form validation test", function () {
        var parseClassName = function (str) {
            return str.split(" ");
        }, requiredFields = [
            {
                "name": "sender_name",
                "checMark": true
            }, {
                "name": "sender_email",
                "checkMark": true
            }, {
                "name": "message",
                "checkMark": false
            }
        ];

        beforeEach(function () {
            browser.get("/#/contact");
        });

        requiredFields.forEach(function (field) {
            describe("For " + field.name + " field", function () {
                var target, input, mark;
                beforeEach(function () {
                    target = element.all(by.id(field.name + "_form")).first();
                    input = target.element(by.model("form." + field.name));
                    mark = target.element(by.id(field.name + "_mark"));
                });
                it("The field should be as-is", function () {
                    target.getAttribute("class").then(function (value) {
                        expect(parseClassName(value).indexOf("has-success") < 0).toBeTruthy();
                        expect(parseClassName(value).indexOf("has-error") < 0).toBeTruthy();
                    });
                    expect(mark.isPresent()).toBeFalsy();
                });
                describe("Input operations", function () {
                    beforeEach(function () {
                        input.getAttribute("type").then(function (value) {
                            if (value === "email") {
                                input.sendKeys("test@example.com");
                            } else {
                                input.sendKeys("Test Example");
                            }
                        });
                    });
                    it("The field should be valid", function () {
                        target.getAttribute("class").then(function (value) {
                            expect(parseClassName(value).indexOf("has-success") >= 0).toBeTruthy();
                            expect(parseClassName(value).indexOf("has-error") < 0).toBeTruthy();
                        });
                        if (field.checkMark) {
                            expect(mark.isDisplayed()).toBeTruthy();
                            mark.getAttribute("class").then(function (value) {
                                expect(parseClassName(value).indexOf("glyphicon-ok") >= 0).toBeTruthy();
                                expect(parseClassName(value).indexOf("glyphicon-warning-sign") < 0).toBeTruthy();
                            });
                        }
                    });
                    it("The field should be invalid when it is clear", function () {
                        input.clear();
                        target.getAttribute("class").then(function (value) {
                            expect(parseClassName(value).indexOf("has-success") < 0).toBeTruthy();
                            expect(parseClassName(value).indexOf("has-error") >= 0).toBeTruthy();
                        });
                        if (field.checkMark) {
                            expect(mark.isDisplayed()).toBeTruthy();
                            mark.getAttribute("class").then(function (value) {
                                expect(parseClassName(value).indexOf("glyphicon-ok") < 0).toBeTruthy();
                                expect(parseClassName(value).indexOf("glyphicon-warning-sign") >= 0).toBeTruthy();
                            });
                        }
                    });
                });
            });
        });

        describe("For email fields", function () {
            var target, input, mark;
            beforeEach(function () {
                target = element.all(by.id("sender_email_form")).first();
                input = target.element(by.model("form.sender_email"));
                mark = target.element(by.id("sender_email_mark"));
            });
            it(
                "The field should be invalid for non-formatted text",
                function () {
                    input.sendKeys("test");
                    target.getAttribute("class").then(function (value) {
                        expect(parseClassName(value).indexOf("has-success") < 0).toBeTruthy();
                        expect(parseClassName(value).indexOf("has-error") >= 0).toBeTruthy();
                    });

                    expect(mark.isDisplayed()).toBeTruthy();
                    mark.getAttribute("class").then(function (value) {
                        expect(parseClassName(value).indexOf("glyphicon-ok") < 0).toBeTruthy();
                        expect(parseClassName(value).indexOf("glyphicon-warning-sign") >= 0).toBeTruthy();
                    });
                }
            );
            it("SHould be invalid for formatted, but tricky email", function () {
                input.sendKeys("test@example");
                target.getAttribute("class").then(function (value) {
                    expect(parseClassName(value).indexOf("has-success") < 0).toBeTruthy();
                    expect(parseClassName(value).indexOf("has-error") >= 0).toBeTruthy();
                });

                expect(mark.isDisplayed()).toBeTruthy();
                mark.getAttribute("class").then(function (value) {
                    expect(parseClassName(value).indexOf("glyphicon-ok") < 0).toBeTruthy();
                    expect(parseClassName(value).indexOf("glyphicon-warning-sign") >= 0).toBeTruthy();
                });
            });
        });
        describe("Oops sign", function () {
            var email, select, oops,
                checkMock = function (code) {
                    /*global angular*/
                    angular.module("checkMock", [
                        "ngMockE2E"
                    ]).run(function ($httpBackend) {
                        /*jslint regexp: true*/
                        $httpBackend.whenGET(
                            /\/contact\/check\/[0-9,a-f]{40}\?sender\=.+/
                        ).respond(code);
                        $httpBackend.whenGET(
                            /.*/
                        ).passThrough();
                    });
                },
                manupulate = function () {
                    email.sendKeys("test@example.com");
                    select.click();
                    select.all(by.tagName("option")).get(1).click();
                    email.click();
                };
            beforeEach(function () {
                email = element.all(by.model("form.sender_email")).first();
                select = element.all(by.model("form.recipient_address")).first();
                oops = element.all(
                    by.id("oops_sign")
                ).first();
            });
            afterEach(function () {
                browser.clearMockModules();
            });
            it("Should be shown", function () {
                browser.addMockModule("checkMock", checkMock, 404);
                browser.refresh();
                manupulate();
                expect(oops.isDisplayed()).toBeTruthy();
            });
            it("Shouldn't be shown", function () {
                browser.addMockModule("checkMock", checkMock, 200);
                browser.refresh();
                manupulate();
                expect(oops.isDisplayed()).toBeFalsy();
            });
            it("Shouldn't be shown when re-editing email", function () {
                browser.addMockModule("checkMock", checkMock, 404);
                browser.refresh();
                manupulate();
                email.clear();
                expect(oops.isDisplayed()).toBeFalsy();
            });
            it("Shouldn't be shown when re-selecting developer", function () {
                browser.addMockModule("checkMock", checkMock, 404);
                browser.refresh();
                manupulate();
                select.click();
                select.all(by.tagName("option")).get(2).click();
                expect(oops.isDisplayed()).toBeFalsy();
            });
        });

        describe("Send alert test", function () {
            var mailBackendMock = function (code, data) {
                /*global angular*/
                angular.module("mailBackendMock", [
                    "ngMockE2E"
                ]).run(function ($httpBackend) {
                    $httpBackend.whenPOST(
                        /\/contact\/[0-9,a-f]{40}/
                    ).respond(code, data);
                    /*jslint regexp: true*/
                    $httpBackend.whenGET(
                        /\/contact\/check\/[0-9,a-f]{40}\?sender\=.+/
                    ).respond(200);
                    $httpBackend.whenGET(
                        /.*/
                    ).passThrough();
                });
            }, senderName,
                senderEmail,
                recipientSelect,
                recipientAddress,
                message,
                sendBtn,
                statusMessage,
                successAdditionalInfo,
                successMessage,
                failureMessage,
                manipulate = function () {
                    senderName.sendKeys("Test Example");
                    senderEmail.sendKeys("test@example.com");
                    recipientSelect.click();
                    recipientAddress.click();
                    message.sendKeys("This is a test");
                };
            beforeEach(function () {
                senderName = element.all(
                    by.model("form.sender_name")
                ).first();
                senderEmail = element.all(
                    by.model("form.sender_email")
                ).first();
                recipientSelect = element.all(
                    by.model("form.recipient_address")
                ).first();
                recipientAddress = recipientSelect.all(
                    by.tagName("option")
                ).get(1);
                message = element.all(
                    by.model("form.message")
                ).first();
                sendBtn = element.all(
                    by.buttonText("Send!")
                ).first();
                statusMessage = element(by.id("status"));
                successMessage = statusMessage.element(
                    by.id("success-message")
                );
                successAdditionalInfo = successMessage.element(
                    by.id("success-devel-message")
                );
                failureMessage = statusMessage.element(
                    by.id("failure-message")
                );
            });
            afterEach(function () {
                browser.clearMockModules();
            });

            it("Status message shouldn't be generated", function () {
                manipulate();
                expect(statusMessage.isPresent()).toBeFalsy();
            });

            it("Should show success message", function () {
                var resultmsg = "Your message has been successfully sent!";
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    200,
                    {
                        "success": resultmsg
                    }
                );
                browser.refresh();
                manipulate();
                expect(sendBtn.isEnabled()).toBeTruthy();
                sendBtn.click();
                expect(statusMessage.isDisplayed()).toBeTruthy();
                expect(successAdditionalInfo.isPresent()).toBeFalsy();
                expect(failureMessage.isPresent()).toBeFalsy();
                statusMessage.getAttribute("class").then(function (clstr) {
                    var classList = parseClassName(clstr);
                    expect(classList).toContain("alert-success");
                    expect(classList).not.toContain("alert-warning");
                    expect(classList).not.toContain("alert-danger");
                });
                expect(successMessage.getText()).toEqual(resultmsg);
            });

            it("Should show success message with additional info", function () {
                var resultObj = {
                    "success": "Your message has been successfully sent!",
                    "additional_info": {
                        "from": "test@example.com",
                        "to": "admin@hysoftware.net",
                        "subject": "Test Message from hysoft",
                        "body": "This is a test"
                    }
                };
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    200,
                    resultObj
                );
                browser.refresh();
                manipulate();
                sendBtn.click();
                expect(successAdditionalInfo.isDisplayed()).toBeTruthy();
                expect(failureMessage.isPresent()).toBeFalsy();
                successAdditionalInfo.getText().then(function (text) {
                    /*global JSON*/
                    var info_obj = JSON.parse(text);
                    expect(
                        info_obj
                    ).toEqual(
                        resultObj.additional_info
                    );
                });
            });

            it("Should't generate success message when errror", function () {
                var resultObj = {
                    "error": 417,
                    "sender_mail": ["Invalid value"]
                };
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    417,
                    resultObj
                );
                browser.refresh();
                manipulate();
                sendBtn.click();
                expect(statusMessage.isDisplayed()).toBeTruthy();
                expect(successMessage.isPresent()).toBeFalsy();
            });
            it("Should show failure section when 417 error", function () {
                var resultObj = {"error": 417};
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    417,
                    resultObj
                );
                browser.refresh();
                manipulate();
                sendBtn.click();
                expect(failureMessage.isDisplayed()).toBeTruthy();
                statusMessage.getAttribute("class").then(function (clstr) {
                    var classList = parseClassName(clstr);
                    expect(classList).toContain("alert-warning");
                    expect(classList).not.toContain("alert-success");
                    expect(classList).not.toContain("alert-danger");
                });
            });
            it("Should show failure section when 500 error", function () {
                var resultObj = {"error": 500};
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    417,
                    resultObj
                );
                browser.refresh();
                manipulate();
                sendBtn.click();
                expect(failureMessage.isDisplayed()).toBeTruthy();
                statusMessage.getAttribute("class").then(function (clstr) {
                    var classList = parseClassName(clstr);
                    expect(classList).not.toContain("alert-warning");
                    expect(classList).not.toContain("alert-success");
                    expect(classList).toContain("alert-danger");
                });
            });
            it("The detail should be shown when error", function () {
                var resultObj = {
                    "error": 417,
                    "backend": ["Test Issue"],
                    "sender_name": ["You're a spammer, aren't your?"]
                }, problemKey = element.all(
                    by.className("problem-key")
                ), problemValue = element.all(
                    by.className("problem-value")
                );
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    417,
                    resultObj
                );
                browser.refresh();
                manipulate();
                sendBtn.click();
                expect(problemKey.count()).toEqual(2);
                expect(problemValue.count()).toEqual(2);
            });
            it("Form data text should be shown when 500 error", function () {
                var resultObj = {
                    "error": 500,
                    "backend": ["Test Issue"]
                }, criticalFormCode = element(by.id("critical-form-code"));
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    500,
                    resultObj
                );
                browser.refresh();
                manipulate();
                sendBtn.click();
                expect(criticalFormCode.isDisplayed()).toBeTruthy();
            });
            it("Form data text should be the form when 500 error", function () {
                var resultObj = {
                    "error": 500,
                    "backend": ["Test Issue"]
                }, criticalFormCode = element(by.id("critical-form-code"));
                browser.addMockModule(
                    "mailBackendMock",
                    mailBackendMock,
                    500,
                    resultObj
                );
                browser.refresh();
                manipulate();
                sendBtn.click();

                criticalFormCode.getText().then(function (text) {
                    /*global JSON*/
                    var formData = JSON.parse(text),
                        formDataKeys = Object.keys(formData.form),
                        errorData = formData.error;
                    expect(formDataKeys).toContain("sender_name");
                    expect(formDataKeys).toContain("sender_email");
                    expect(formDataKeys).toContain("recipient_address");
                    expect(formDataKeys).toContain("message");
                    expect(errorData).toEqual(resultObj);
                });
            });
        });
    });
}(describe, beforeEach, afterEach, it, expect, browser, element, by));
