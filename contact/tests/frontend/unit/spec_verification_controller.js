/*global describe, beforeEach, afterEach, it, expect, inject, module, spyOn*/
(function (describe, beforeEach, afterEach, it, expect, inject, module, spyOn) {
    "use strict";
    describe("Verify Email Controller unit tests", function () {
        var scope, controller;
        beforeEach(function () {
            module("hysoft.contact.controller");
        });
        beforeEach(inject(function ($rootScope, $controller) {
            scope = $rootScope.$new();
            controller = $controller("VerificationController", {
                "$scope": scope,
                "$stateParams": {
                    "token": "50f1395980150811371f5adb2955ed8505a424b4"
                }
            });
        }));
        afterEach(function () {
            scope.$destroy();
            controller = null;
            scope = null;
        });
        it("Controller should be defnied", function () {
            expect(controller).toBeDefined();
        });
        it("send should be defined", function () {
            expect(scope.send).toBeDefined();
        });
        it("Calling send, scope.form.$save should be called", function () {
            if (scope.form.$save) {
                scope.form.$save = function () {
                    return {
                        "catch": function (fn) {
                            return fn({
                                "error": 404,
                                "data": "not found"
                            });
                        }
                    };
                };
            }
            spyOn(scope.form, "$save").and.callThrough();
            scope.send();
            expect(scope.form.$save).toHaveBeenCalled();
        });
        describe("Calling send with 200...", function () {
            beforeEach(inject(function ($httpBackend) {
                $httpBackend.expectPOST(
                    /\/contact\/verify\/[a-f,0-9]{40}/
                ).respond(200, {
                    "success": "Your message has been sent successfully!"
                });
            }));
            afterEach(inject(function ($httpBackend) {
                $httpBackend.verifyNoOutstandingExpectation();
                $httpBackend.verifyNoOutstandingRequest();
            }));
            it("POST request should be thrown", inject(function ($httpBackend) {
                scope.send();
                $httpBackend.flush();
            }));
            it("Success field exists in form", inject(function ($httpBackend) {
                scope.send();
                $httpBackend.flush();
                expect(scope.form.success).toBeDefined();
            }));
        });
        describe("Calling send with error", function () {
            var errObj = {
                "error": 404,
                "backend": "NOT FOUND"
            };
            beforeEach(inject(function ($httpBackend) {
                $httpBackend.expectPOST(
                    /\/contact\/verify\/[a-f,0-9]{40}/
                ).respond(404, errObj);
            }));
            afterEach(inject(function ($httpBackend) {
                $httpBackend.verifyNoOutstandingExpectation();
                $httpBackend.verifyNoOutstandingRequest();
            }));
            it("POST request should be thrown", inject(function ($httpBackend) {
                scope.send();
                $httpBackend.flush();
            }));
            it("The form shouldn't have error", inject(function ($httpBackend) {
                scope.send();
                $httpBackend.flush();
                expect(scope.form.error).not.toBeDefined();
            }));
            it("The error should have error data", inject(function ($httpBackend) {
                scope.send();
                $httpBackend.flush();
                expect(scope.error).toEqual(errObj);
            }));
        });
    });
}(describe, beforeEach, afterEach, it, expect, inject, module, spyOn));
