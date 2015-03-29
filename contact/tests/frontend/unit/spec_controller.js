/*global describe, beforeEach, afterEach,
    it, expect, inject, module, spyOn*/
(function (describe, beforeEach, afterEach,
            it, expect, inject, module, spyOn) {
    "use strict";
    describe("Contact Controller unit tests", function () {
        var controller, scope;
        beforeEach(function () {
            module("hysoft.contact.controller");
        });
        beforeEach(inject(function ($rootScope, $controller) {
            scope = $rootScope.$new();
            controller = $controller(
                "ContactController",
                {
                    "$scope": scope
                }
            );
        }));
        afterEach(function () {
            scope.$destroy();
            scope = null;
            controller = null;
        });
        afterEach(inject(
            function ($httpBackend) {
                $httpBackend.verifyNoOutstandingExpectation();
                $httpBackend.verifyNoOutstandingRequest();
            }
        ));
        it("Controller should be defined", function () {
            expect(controller).toBeDefined();
        });
        describe("checkMailIsInList check", function () {
            it("GET request should be thrown and success", inject(
                function ($httpBackend) {
                    scope.form.sender_email = "test@example.com";
                    scope.form.recipient_address = "test";
                    $httpBackend.expectGET(
                        "/contact/check/" + scope.form.recipient_address +
                            "?sender=" + scope.form.sender_email
                    ).respond(200);
                    scope.checkMailIsInList();
                    $httpBackend.flush();
                    expect(scope.heIsInList).toBeTruthy();
                }
            ));
            it("GET request should be thrown and failure", inject(
                function ($httpBackend) {
                    scope.form.sender_email = "test@example.com";
                    scope.form.recipient_address = "test";
                    $httpBackend.expectGET(
                        "/contact/check/" + scope.form.recipient_address +
                            "?sender=" + scope.form.sender_email
                    ).respond(404);
                    scope.checkMailIsInList();
                    $httpBackend.flush();
                    expect(scope.heIsInList).toBeFalsy();
                }
            ));
        });
        describe("sendForm check", function () {
            /*global xit*/

            it("scope.form.$save should be called", function () {
                spyOn(scope.form, "$save");
                scope.form.recipient_address = "test";
                scope.sendForm();
                expect(
                    scope.form.$save
                ).toHaveBeenCalled();
            });
            it("POST request should be generated", inject(
                function ($httpBackend) {
                    scope.form.recipient_address = "test";
                    scope.form.csrftoken = "hello";
                    $httpBackend.expectPOST(
                        "/contact/" + scope.form.recipient_address
                    ).respond(200, {
                        "success": "Your message has been successfully sent!"
                    });
                    scope.sendForm();
                    $httpBackend.flush();
                    expect(scope.form.sender_name).toBeFalsy();
                    expect(scope.form.sender_email).toBeFalsy();
                    expect(scope.form.recipient_address).toBeFalsy();
                    expect(scope.form.message).toBeFalsy();
                    expect(scope.form.success).toBeTruthy();
                }
            ));
        });
    });
}(describe, beforeEach, afterEach,
    it, expect, inject, module, spyOn));
