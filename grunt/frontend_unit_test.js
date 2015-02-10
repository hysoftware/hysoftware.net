/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js");
    e.karma = {
        "options": {
            "basePath": "./",
            "frameworks": ['jasmine'],
            "reporters": ['progress'],
            "port": 9876,
            "colors": true,
            "logLevel": "INFO",
            "autoWatch": false,
            "files": ["home/static/third_party.js"].concat(
                common.frontend.js,
                common.tests.unit.frontend,
                "!home/static/third_party/**/*.js",
                "!home/static/assets.js"
            )
        },
        "dev": {
            "browsers": [
                "Chrome",
                "Firefox",
                "PhantomJS"
            ],
            "background": true,
            "singleRun": false
        },
        "CI": {
            "browsers": [
                "PhantomJS"
            ],
            "singleRun": true
        }
    };
}(exports, require));
