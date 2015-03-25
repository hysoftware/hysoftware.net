/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js"),
        pathJoin = r("path").join,
        files = [
            "manage.py"
        ].concat(common.hysoft_modules).join(" "),
        backend_syntax_test_commands = [
            "flake8 -j auto --exclude=" + common.exclude.backend.join(",") +
                " " + files,
            "pylint --disable=locally-disabled,locally-enabled --ignore=migrations " + files
        ],
        backend_test_commands = [
            "python manage.py migrate",
            "python manage.py loaddata " + [
                "about/fixtures/hiroaki.json"
            ].join(" "),
            "python manage.py test"
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
