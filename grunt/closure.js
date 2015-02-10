/*global require, exports*/
(function (r, e) {
    "use strict";
    var third_party_files = r("./third_party_uglify").third_party_files,
        common = r("./common"),
        srcList = common.frontend.js.concat(
            common.exclude.frontend.js.map(function (file) {
                return "!" + file;
            }).concat(common.tests.unit.frontend.map(function (file) {
                return "!" + file;
            }))
        );
    e.closureCompiler = {
        "options": {
            "compilerFile": "./tools/closure-compiler/compiler.jar",
            "checkModified": true,
            "execOpts": {
                "maxBuffer": 1073741824
            }
        },
        "dev": {
            "options": {
                "compilerOpts": {
                    "create_source_map": "home/static/assets.js.map",
                    "compilation_level": "ADVANCED",
                    "angular_pass": null,
                    "externs": third_party_files,
                    "language_in": "ECMASCRIPT5",
                    "warning_level": "QUIET"
                }
            },
            "dest": "home/static/assets.js",
            "src": srcList
        },
        "production": {
            "options": {
                "compilerOpts": {
                    "compilation_level": "ADVANCED",
                    "angular_pass": null,
                    "externs": third_party_files,
                    "language_in": "ECMASCRIPT5",
                    "warning_level": "QUIET"
                }
            },
            "dest": "home/static/assets.js",
            "src": srcList
        }
    };
}(require, exports));
