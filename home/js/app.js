/*global angular*/

(function (a) {
    "use strict";
    a.module("hysoft", [
        "ui.router",
        "ngRoute",
        "hysoft.home.routes"
    ]).config([
        "$routeProvider",
        "$locationProvider",
        "$compileProvider",
        function (routeProvider, locationProvider, compileProvider) {
            compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|data):/);
            routeProvider.otherwise("/404");
            locationProvider.html5Mode({
                "enabled": true,
                "requireBase": false
            });
        }
    ]);
}(angular));
