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
        it("Controller should be defined", function () {
            expect(controller).toBeDefined();
        });
    });
}(describe, beforeEach, afterEach, it, expect, inject, module));
