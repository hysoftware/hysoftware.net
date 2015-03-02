/*global angular*/

(function (a) {
    "use strict";
    a.module("hysoft", [
        "ngRoute"
    ]).config([
        "$urlRouterProvider",
        "$locationProvider",
        "$compileProvider",
        function (routeProvider, locationProvider, compileProvider) {
            compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|data):/);
            locationProvider.html5Mode(true);
            routeProvider.otherwise("/404");
        }
    ]);
}(angular));
