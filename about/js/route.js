/*global angular*/
(function (a) {
    "use strict";
    a.module("hysoft.about.routes", [
        "ui.router"
    ]).config([
        "$stateProvider",
        function (stateProvider) {
            stateProvider.state("about", {
                "url": "/about",
                "templateUrl": "about"
            });
        }
    ]);
}(angular));
