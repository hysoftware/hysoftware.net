/*global angular*/

(function (a) {
    "use strict";
    a.module("hysoft", [
        "ui.router",
        "ngRoute",
        "ngCookies",
        "hysoft.home.routes",
        "hysoft.about.routes",
        "hysoft.contact.route"
    ]).config([
        "$urlRouterProvider",
        "$locationProvider",
        "$compileProvider",
        "$httpProvider",
        function (urlRouterProvider, locationProvider, compileProvider, httpProvider) {
            compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|data):/);
            urlRouterProvider.otherwise("/");
            locationProvider.html5Mode(true);
            httpProvider.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";
        }
    ]).run([
        "$rootScope",
        "$state",
        "$cookies",
        "$http",
        function (rootScope, state, cookies, httpProvider) {
            /*jslint sub:true*/
            rootScope.state = state;
            if (a.version.major >= 1 && a.version.minor > 3) {
                httpProvider.defaults.headers.common["X-CSRFToken"] =  cookies.get("csrftoken");
            } else {
                httpProvider.defaults.headers.common["X-CSRFToken"] =  cookies["csrftoken"];
            }
        }
    ]);
}(angular));
