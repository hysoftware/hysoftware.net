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
        describe("Incorrect Input", function () {
            var inputGroup,
                submitBtn,
                input,
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
        });
        describe("Correct Input", function () {
            var input, inputGroup, sendBtn;
            describe("Success return without debug", function () {
                beforeEach(function () {
                    browser.addMockModule(
                        "backendMock",
                        backendMock,
                        200,
                        {"success": "Your message has been successfully sent!"}
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
                });
                it("Email input should be success state", function () {
                    inputGroup.getAttribute("class").then(function (value) {
                        var className = parseClassName(value);
                        expect(className).not.toContain("has-error");
                        expect(className).toContain("has-success");
                    });
                });
                describe("After transaction", function () {
                    beforeEach(function () {
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
                });
            });
        });
    });
}(describe, beforeEach, afterEach, it, expect,
    browser, element, by, require));
