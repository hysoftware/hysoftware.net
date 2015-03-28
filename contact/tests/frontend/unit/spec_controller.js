/*global describe, beforeEach, afterEach, it, expect, inject, module*/
(function (describe, beforeEach, afterEach, it, expect, inject, module) {
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
                        "/contact/check/" + scope.form.recipient_address
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
                        "/contact/check/" + scope.form.recipient_address
                    ).respond(404);
                    scope.checkMailIsInList();
                    $httpBackend.flush();
                    expect(scope.heIsInList).toBeFalsy();
                }
            ));
        });
    });
}(describe, beforeEach, afterEach, it, expect, inject, module));
