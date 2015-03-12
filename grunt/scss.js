/*global exports*/
(function (e) {
    "use strict";
    e.output_path = "./home/static/assets.css";
    e.sass = {
        "options": {
            "bundleExec": true,
            "unixNewlines": true,
            "style": "compressed"
        },
        "dev": {
            "files": {
                "./home/static/assets.css": "./hysoft/scss/main.scss"
            }
        },
        "production": {
            "options": {
                "sourcemap": "none",
                "noCache": true
            },
            "files": {
                "./home/static/assets.css": "./hysoft/scss/main.scss"
            }
        }
    };
}(exports));
