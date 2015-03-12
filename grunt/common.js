/*global exports, require*/
(function (exp, r) {
    "use strict";
    var join = r("path").join;
    exp.hysoft_modules = [
        "about",
        "contact",
        "home",
        "hysoft"
    ];

    exp.gruntFile = [
        "grunt/**/*.js",
        "Gruntfile.js"
    ];
    exp.frontend = {
        "js": exp.hysoft_modules.map(function (el) {
            return join(el, "js/**/*.js");
        }),
        "scss": exp.hysoft_modules.map(function (el) {
            return join(el, "scss/**/*.scss");
        })
    };
    exp.backend = ["manage.py"].concat(
        exp.hysoft_modules.map(function (el) {
            return join(el, "**/*.py");
        })
    );
    exp.tests = {
        "unit": {
            "frontend": exp.hysoft_modules.map(function (hy_module) {
                return join(hy_module, "tests/frontend/unit/**/*.js");
            })
        },
        "e2e": {
            "frontend": exp.hysoft_modules.map(function (hy_module) {
                return join(hy_module, "tests/frontend/e2e/**/*.js");
            })
        },
        "all": {
            "frontend": exp.hysoft_modules.map(function (hy_module) {
                return join(hy_module, "tests/frontend/**/*.js");
            })
        }
    };
    exp.tasks = {
        "common": {
            "frontend": [
                "jslint:frontend"
            ]
        }
    };
    exp.tasks.dev = {
        "frontend": exp.tasks.common.frontend,
        "backend": [
            "shell:backend-syntax-check-dev"
        ]
    };
    exp.tasks.production = {
        "frontend": exp.tasks.common.frontend,
        "backend": [
            "shell:backend-syntax-check-ci"
        ]
    };
    exp.tasks.dev.frontend = exp.tasks.dev.frontend.concat([
        "karma:dev:run",
        "closureCompiler:dev",
        "sass:dev",
        "autoprefixer:dev"
    ]);
    exp.tasks.production.frontend = exp.tasks.production.frontend.concat([
        "karma:CI",
        "closureCompiler:production",
        "sass:production",
        "autoprefixer:production"
    ]);
    exp.exclude = {
        "frontend": {
            "js": [
                "node_modules/**/*.js",
                "**/*.min.js",
                "home/static/third_party/**/*.js",
                "home/static/third_party.js",
                "home/static/assets.js"
            ]
        },
        "backend": [
            ".svn",
            "CVS",
            ".bzr",
            ".hg",
            ".git",
            "__pycache__",
            ".tox",
            "migrations"
        ]
    };
}(exports, require));
