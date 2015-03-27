/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.controller", [
        "hysoft.contact.resource"
    ]).controller("ContactController", [
        "$scope",
        function (scope) {
            scope.dummy = {};
            return undefined;
        }
    ]);
}(angular));
