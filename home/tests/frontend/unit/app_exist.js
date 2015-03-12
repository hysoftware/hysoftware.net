/*global describe, it, expect, angular*/
(function (describe, it, expect, angular) {
    "use strict";
    describe("Application Existence Tests", function () {
        it("Check if the app exists", function () {
            var hysoft_module = angular.module("hysoft");
            expect(hysoft_module).toBeTruthy();
        });
    });
}(describe, it, expect, angular));
