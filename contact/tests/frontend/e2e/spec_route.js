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
            ).first();
            expect(title.isDisplayed()).toBeTruthy();
        });
    });
    describe("Verificatoin E2E tests (Route)", function () {
        beforeEach(function () {
            browser.get(
                "/contact/verify/50f1395980150811371f5adb2955ed8505a424b4"
            );
        });
        it("The route should be matched with /contact/verify", function () {
            expect(
                browser.getLocationAbsUrl()
            ).toMatch(
                /\/contact\/verify\/50f1395980150811371f5adb2955ed8505a424b4$/
            );
        });
        it("The page should be verification page", function () {
            var title = element.all(
                by.css("article.mail-verification")
            ).first();
            expect(title.isDisplayed()).toBeTruthy();
        });
    });
}(describe, beforeEach, it, expect, browser, element, by));
