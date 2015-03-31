/*global exports, require*/

(function (e, r) {
    "use strict";
    var common = r("./common.js");
    e.protractor = {};
    // Browsers to create E2E target
    [
        "chrome",
        "firefox",
        "phantomJS"
    ].forEach(function (browser) {
        e.protractor[browser] = {
            "options": {
                "configFile": "./protractor/conf.js",
                "args": {
                    "baseUrl": "http://localhost:50000",
                    "framework": "jasmine2",
                    "capabilities": {
                        "browserName": browser
                    },
                    "specs": common.tests.e2e.frontend
                }
            }
        };
        if (browser === "chrome" || browser === "firefox") {
            e.protractor[browser].options.args.directConnect = true;
        }
    });
}(exports, require));
