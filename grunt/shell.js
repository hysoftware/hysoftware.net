/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js"),
        files = [
            "manage.py"
        ].concat(common.hysoft_modules).join(" "),
        backend_test_commands = [
            "echo flake8",
            "flake8 -j auto --exclude=" + common.exclude.backend.join(",") +
                " " + files,
            "echo pylint",
            "pylint --disable=locally-disabled,locally-enabled --ignore=migrations " + files,
            "echo python manage.py migrate",
            "python manage.py migrate",
            "echo python manage.py loaddata",
            "python manage.py loaddata " + [
                "about/fixtures/hiroaki.json"
            ].join(" "),
            "echo python manage.py test",
            "python manage.py test"
        ];
    e.shell = {
        "backend-syntax-check-dev": {
            "command": [].concat(
                "source ../bin/activate",
                backend_test_commands,
                "deactivate"
            ).join("&&")
        },
        "backend-syntax-check-ci": {
            "command": backend_test_commands.join("&&")
        }
    };
}(exports, require));
