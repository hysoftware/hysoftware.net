/*global describe, beforeEach, afterEach, it, expect,
    browser, element, by, require*/
(function (describe, beforeEach, afterEach, it, expect,
            browser, element, by, req) {
    "use strict";
    /*jslint unparam: true*/
    describe("Mail Verification Form E2E test", function () {
        var parseClassName = req("./class_parser.js").parseClassName,
            backendMock = function (code, data) {
                /*global angular*/
                angular.module("backendMock", [
                    "ngMockE2E"
                ]).run(function ($httpBackend) {
                    $httpBackend.whenPOST(
                        /\/contact\/verify\/[a-f,0-9]{40}/
                    ).respond(code, data);
                    /*jslint regexp: true*/
                    $httpBackend.whenGET(
                        /.*/
                    ).passThrough();
                });
            };
        afterEach(function () {
            browser.clearMockModules();
        });
        it("Submit button should be disabled", function () {
            browser.get(
                "/contact/verify/50f1395980150811371f5adb2955ed8505a424b4"
            );
            var submitBtn = element.all(
                by.buttonText("Send!")
            ).first();
            expect(submitBtn.isDisplayed()).toBeTruthy();
            expect(submitBtn.isEnabled()).toBeFalsy();
        });
        it("Email input should be neither error nor success state", function () {
            browser.get(
                "/contact/verify/50f1395980150811371f5adb2955ed8505a424b4"
            );
            var inputGroup = element.all(
                by.id("email-form-group")
            ).first();
            inputGroup.getAttribute("class").then(function (value) {
                var className = parseClassName(value);
                expect(className).not.toContain("has-error");
                expect(className).not.toContain("has-success");
            });
        });
        it("Status shouldn't be generated", function () {
            browser.get(
                "/contact/verify/50f1395980150811371f5adb2955ed8505a424b4"
            );
            var status = element(by.id("status"));
            expect(status.isPresent()).toBeFalsy();
        });
        describe("Incorrect Input", function () {
            var inputGroup,
                submitBtn,
                input,
                status,
                expectError = function () {
                    inputGroup.getAttribute("class").then(function (value) {
                        var className = parseClassName(value);
                        expect(className).toContain("has-error");
                        expect(className).not.toContain("has-success");
                    });
                    expect(submitBtn.isDisplayed()).toBeTruthy();
                    expect(submitBtn.isEnabled()).toBeFalsy();
                };
            beforeEach(function () {
                browser.get(
                    "/contact/verify/50f1395980150811371f5adb2955ed8505a424b4"
                );
                inputGroup = element.all(by.id("email-form-group")).first();
                input = element.all(by.model("form.email")).first();
                submitBtn = element.all(
                    by.buttonText("Send!")
                ).first();
            });
            it("\"test\" should be invalid", function () {
                input.sendKeys("test");
                expectError();
            });
            it("\"test@example\" should be invalid", function () {
                input.sendKeys("test@example");
                expectError();
            });
            it("Status shouldn't be generated", function () {
                status = element(by.id("status"));
                expect(status.isPresent()).toBeFalsy();
            });
        });
        describe("Correct Input", function () {
            var input, inputGroup, sendBtn, status, additional;
            describe("Form check", function () {
                beforeEach(function () {
                    browser.get(
                        "/contact/verify/50f1395980150811371f5adb2955ed8505a424b4"
                    );
                    inputGroup = element.all(by.id("email-form-group")).first();
                    input = element.all(by.model("form.email")).first();
                    input.sendKeys("test@example.com");
                    sendBtn = element.all(by.buttonText("Send!")).first();
                    status = element(by.id("status"));
                    additional = element(by.id("additional"));
                });
                it("Email input should be success state", function () {
                    inputGroup.getAttribute("class").then(function (value) {
                        var className = parseClassName(value);
                        expect(className).not.toContain("has-error");
                        expect(className).toContain("has-success");
                    });
                });
                it("Button should be enabled", function () {
                    expect(sendBtn.isEnabled()).toBeTruthy();
                });
                it("Status should't be generated", function () {
                    expect(status.isPresent()).toBeFalsy();
                });
            });
            describe("Success return", function () {
                var start = function (additionalInfo) {
                    /*jslint nomen: true*/
                    var successObj = {
                        "success": "Your message has been successfully sent!"
                    };
                    if (additionalInfo) {
                        successObj.additional_info = additionalInfo;
                    }
                    browser.addMockModule(
                        "backendMock",
                        backendMock,
                        200,
                        successObj
                    );
                    browser.get(
                        "/contact/verify/50f1395980150811371f5adb2955ed8505a424b4"
                    );
                    inputGroup = element.all(by.id("email-form-group")).first();
                    input = element.all(by.model("form.email")).first();
                    input.sendKeys("test@example.com");
                    sendBtn = element.all(
                        by.buttonText("Send!")
                    ).first();
                    status = element(by.id("status"));
                };
                describe("without debug info", function () {
                    beforeEach(function () {
                        start();
                        sendBtn.click();
                    });
                    it("sendBtn should be disabled", function () {
                        expect(sendBtn.isDisplayed()).toBeTruthy();
                        expect(sendBtn.isEnabled()).toBeFalsy();
                    });
                    it("input should be disabled", function () {
                        expect(input.isDisplayed()).toBeTruthy();
                        expect(input.isEnabled()).toBeFalsy();
                    });
                    it("Status should be Displayed", function () {
                        expect(status.isDisplayed()).toBeTruthy();
                        status.getAttribute("class").then(function (value) {
                            expect(
                                parseClassName(value)
                            ).toContain("alert-success");
                        });
                    });
                    it("Status text and success text should be the same",
                        function () {
                            expect(status.getText()).toEqual(
                                "Your message has been successfully sent!"
                            );
                        });
                    it("additional shouldn't be provided", function () {
                        expect(additional.isPresent()).toBeFalsy();
                    });
                });
            });
        });
    });
}(describe, beforeEach, afterEach, it, expect,
    browser, element, by, require));
