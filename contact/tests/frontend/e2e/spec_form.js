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
                "Inputting non-email formatted text, the field should be invalid",
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
    });
}(describe, beforeEach, afterEach, it, expect, browser, element, by));
