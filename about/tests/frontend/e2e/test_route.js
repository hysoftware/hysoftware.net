/*global describe, beforeEach, it, expect, browser, element, by, angular*/
(function (describe, beforeEach, it, expect,
            browser, element, by) {
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
        describe("Contents check", function () {
            beforeEach(function () {
                browser.get("/about");
            });
            it("The page should have about article", function () {
                var article = element.all(by.css("article.about"));
                expect(article.isDisplayed()).toBeTruthy();
            });
        });
    });
}(describe, beforeEach, it, expect, browser, element, by));
