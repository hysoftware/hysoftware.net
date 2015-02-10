/*global describe, beforeEach, afterEach, it, expect, inject, module*/

(function (describe, beforeEach, afterEach, it, expect, inject, module) {
    "use strict";
    describe("Main controller unit tests", function () {
        var scope,
            controller;
        beforeEach(function () {
            module("hysoft.home.controllers");
        });
        beforeEach(inject(function ($controller, $rootScope) {
            scope = $rootScope.$new();
            controller = $controller("homeController", {
                "$scope": scope
            });
        }));
        afterEach(function () {
            scope.$destroy();
        });
        it("The controller should be defined", function () {
            expect(controller).toBeDefined();
        });
    });
}(describe, beforeEach, afterEach, it, expect, inject, module));
