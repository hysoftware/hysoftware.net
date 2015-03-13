/*global angular*/

(function (a) {
    "use strict";
    a.module("hysoft", [
        "ui.router",
        "ngRoute",
        "hysoft.home.routes",
        "hysoft.about.routes"
    ]).config([
        "$routeProvider",
        "$locationProvider",
        "$compileProvider",
        "$httpProvider",
        function (routeProvider, locationProvider, compileProvider, httpProvider) {
            compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|data):/);
            routeProvider.otherwise("/404");
            locationProvider.html5Mode({
                "enabled": true,
                "requireBase": false
            });
            httpProvider.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";
        }
    ]);
}(angular));
