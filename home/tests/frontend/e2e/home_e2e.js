/*global describe, beforeEach, it, expect, browser*/
(function (describe, beforeEach, it, expect, browser) {
    "use strict";
    describe("Home page e2e test", function () {
        beforeEach(function () {
            browser.get("#/");
        });
        it("The URL should be /.", function () {
            expect(browser.getLocationAbsUrl()).toMatch(
                /^\/$/
            );
        });
    });
}(describe, beforeEach, it, expect, browser));
