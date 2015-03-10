/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js"),
        files = [
            "manage.py"
        ].concat(common.hysoft_modules).join(" "),
        backend_syntax_commands = [
            "flake8 -j auto --exclude=" + common.exclude.backend.join(",") +
                " " + files,
            "pylint --ignore=migrations " + files
        ];
    e.shell = {
        "backend-syntax-check-dev": {
            "command": [].concat(
                "source ../bin/activate",
                backend_syntax_commands,
                "deactivate"
            ).join("&&")
        },
        "backend-syntax-check-ci": {
            "command": backend_syntax_commands.join("&&")
        }
    };
}(exports, require));
