/*global exports, require*/
(function (e, r) {
    "use strict";
    var path = r("path"),
        third_party_path = "home/static/third_party",
        build_order = [
            "jquery/dist/jquery.js",
            "bootstrap/dist/js/bootstrap.js",
            "modernizr/modernizr.js",
            "detectizr/dist/detectizr.js",
            "angular/angular.js",
            "angular-mocks/angular-mocks.js",
            "angular-resource/angular-resource.js",
            "angular-route/angular-route.js",
            "angular-sanitize/angular-sanitize.js",
            "angular-ui-router/release/angular-ui-router.js"
        ];
    e.third_party_files = build_order.map(function (file) {
        return path.join(third_party_path, file);
    });
    e.uglify = {
        "options": {
            "mangle": false
        },
        "dev": {
            "options": {
                "sourceMap": true
            },
            "files": {
                "home/static/third_party.js": build_order.map(
                    function (file) {
                        return path.join(third_party_path, file);
                    }
                )
            }
        },
        "production": {
            "options": {
                "compress": {
                    "drop_console": true
                },
                "mangle": true,
                "sourceMap": false
            },
            "files": {
                "home/static/third_party.js": build_order.map(
                    function (file) {
                        return path.join(third_party_path, file);
                    }
                )
            }
        }
    };
}(exports, require));
