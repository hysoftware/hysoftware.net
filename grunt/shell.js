/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js"),
        files = [
            "manage.py"
        ].concat(common.hysoft_modules).join(" "),
        backend_syntax_test_commands = [
            "flake8 -j auto --exclude=" + common.exclude.backend.join(",") +
                " " + files,
            "pylint -r n --disable=locally-disabled,locally-enabled --ignore=migrations " + files
        ],
        backend_test_commands = [
            "DEBUG=True python manage.py test"
        ];
    e.shell = {
        "backend-syntax-check-dev": {
            "command": [].concat(
                "source ../bin/activate",
                backend_syntax_test_commands,
                backend_test_commands,
                "deactivate"
            ).join("&&")
        },
        "backend-syntax-check-ci": {
            "command": [].concat(
                backend_syntax_test_commands
            ).join("&&")
        }
    };
}(exports, require));
