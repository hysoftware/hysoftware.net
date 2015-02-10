/*global exports, require*/
(function (e, r) {
    "use strict";
    var common = r("./common.js");
    e.watch = {
        "frontend": {
            "files": common.gruntFile.concat(
                [
                    common.frontend.js,
                    common.frontend.scss,
                    common.tests.all.frontend,
                    common.exclude.frontend.js.map(function (file) {
                        return "!" + file;
                    })
                ]
            ),
            "tasks": common.tasks.dev.frontend
        },
        "backend": {
            "files": common.backend.concat(
                common.exclude.backend.map(function (file) {
                    return "!" + file;
                })
            ),
            "tasks": common.tasks.dev.backend
        }
    };
}(exports, require));
