/*global describe, beforeEach, it, expect, browser, element, by*/
(function (describe, beforeEach, it, expect, browser, element, by) {
    "use strict";
    describe("Contact E2E tests (Route)", function () {
        beforeEach(function () {
            browser.get("/contact");
        });
        it("The route should be matched with /contact", function () {
            expect(
                browser.getLocationAbsUrl()
            ).toMatch(/\/contact$/);
        });
        it("The page should be contact page", function () {
            var title = element.all(
                by.css("article.contact")
            );
            expect(title.isDisplayed()).toBeTruthy();
        });
    });
}(describe, beforeEach, it, expect, browser, element, by));
