/*global describe, it, expect, browser, element, by, beforeEach*/
(function (describe, it, expect, browser, element, by, beforeEach) {
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
                var article;
                browser.get("/about");
                article = element.all(by.css("article.about"));
                expect(article.isDisplayed()).toBeTruthy();
            });
        });
    });
}(describe, it, expect, browser, element, by, beforeEach));
