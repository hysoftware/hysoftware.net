/*global angular*/
(function (angular) {
    "use strict";
    angular.module("hysoft.home.controllers", [
    ]).controller("homeController", [
        "$scope",
        function ($scope) {
            /*jslint unparam: true*/
            // Add code and remove return undefined
            $scope.test = 1 + 1;
            return undefined;
        }
    ]);
}(angular));
