/*global describe, it, expect, browser*/
(function (describe, it, expect, browser) {
    "use strict";
    describe("About route test", function () {
        it("The route named about should exist", function () {
            browser.get("/about");
            expect(
                browser.getLocationAbsUrl()
            ).toMatch(
                /\/about$/
            );
        });
    });
}(describe, it, expect, browser));
