/*global module, require*/
(function (m, r) {
    "use strict";
    m.exports = function (grunt) {
        var common = r("./grunt/common.js");
        grunt.initConfig({
            "jslint": r("./grunt/jslint.js").jslint,
            "watch": r("./grunt/watch.js").watch,
            "shell": r("./grunt/shell.js").shell,
            "uglify": r("./grunt/third_party_uglify.js").uglify,
            "closureCompiler": r("./grunt/closure.js").closureCompiler,
            "karma": r("./grunt/frontend_unit_test.js").karma,
            "sass": r("./grunt/scss.js").sass,
            "autoprefixer": r("./grunt/cssprefix.js").autoprefixer
        });

        /* Write tasks for development */
        grunt.registerTask(
            "third_party-dev",
            "Generate third_party.js for development",
            "uglify:dev"
        );
        grunt.registerTask(
            "devFront",
            "Watch frontend scripts for development",
            [
                "karma:dev:start",
                "watch:frontend"
            ]
        );
        grunt.registerTask(
            "devBack",
            "Watch backend scripts for development",
            "watch:backend"
        );

        /* Write tasks for frontend creation */
        grunt.registerTask(
            "third_party",
            "Generate third_party.js for production",
            "uglify:production"
        );
        grunt.registerTask(
            "CIFront",
            "This is just used for CI (frontend)",
            common.tasks.production.frontend
        );
        grunt.registerTask(
            "CIBack",
            "This is just used for CI (backend)",
            common.tasks.production.backend
        );
        r("matchdep").filterDev("grunt-*").forEach(grunt.loadNpmTasks);
    };
}(module, require));
