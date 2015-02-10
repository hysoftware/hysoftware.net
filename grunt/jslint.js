/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js");
    e.jslint = {
        "frontend": {
            "src": common.gruntFile.concat(
                common.frontend.js,
                common.tests.all.frontend
            ),
            "exclude": common.exclude.frontend.js
        }
    };
}(exports, require));
