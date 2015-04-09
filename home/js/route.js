/*global angular*/
(function (angular) {
    "use strict";
    angular.module("hysoft.home.routes", [
        "ui.router",
        "hysoft.home.controllers"
    ]).config([
        "$stateProvider",
        function (stateProvider) {
            stateProvider.state(
                "home",
                {
                    "url": "/",
                    "templateUrl": "/home",
                    "controller": "homeController"
                }
            );
        }
    ]);
}(angular));
