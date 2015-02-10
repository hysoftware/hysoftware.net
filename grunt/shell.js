/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js"),
        files = [
            "manage.py"
        ].concat(common.hysoft_modules).join(" ");
    e.shell = {
        "backend-syntax-check": {
            "command": [
                "source ../bin/activate",
                "flake8 -j auto " +
                    "--exclude=" + common.exclude.backend.join(",") +
                    " " + files,
                "pylint --ignore=migrations " + files,
                "deactivate"
            ].join("&&")
        }
    };
}(exports, require));
