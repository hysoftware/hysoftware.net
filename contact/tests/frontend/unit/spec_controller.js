/*global describe, beforeEach, afterEach,
    it, expect, inject, module, JSON, spyOn*/
(function (describe, beforeEach, afterEach,
            it, expect, inject, module, JSON, spyOn) {
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
            var postResponse = function (code, status, data) {
                return function () {
                    var parsed = JSON.parse(data);
                    expect(parsed.csrftoken).toBeTruthy();
                    return [code, data, {}, status];
                };
            };
            /*global xit*/

            xit("scope.form.$save should be called", function () {
                spyOn(scope.form, "$save");
                scope.form.recipient_address = "test";
                scope.sendForm();
                expect(
                    scope.form.$save
                ).toHaveBeenCalled();
            });
            xit("POST request should be generated", inject(
                function ($httpBackend) {
                    scope.recipient_address = "test";
                    $httpBackend.expectPOST(
                        "/contact/" + scope.recipient_address
                    ).respond(
                        postResponse(200, "OK", "")
                    );
                    scope.sendForm();
                    $httpBackend.flush();
                    expect(scope.form.sender_name).toBeFalsy();
                    expect(scope.form.sender_email).toBeFalsy();
                    expect(scope.form.recipient_address).toBeFalsy();
                    expect(scope.form.message).toBeFalsy();
                }
            ));
        });
    });
}(describe, beforeEach, afterEach,
    it, expect, inject, module, JSON, spyOn));
