/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.controller", [
        "ngCookies",
        "hysoft.contact.resource"
    ]).controller("ContactController", [
        "$scope",
        "$cookies",
        "ListChecker",
        function (scope, cookies, ListChecker) {
            /*jslint sub: true*/

            // This trick is needed to avoid demangle
            // compression from closure compiler.
            scope["form"] = {};
            scope["clearMailIsInList"] = function () {
                scope["heIsInList"] = undefined;
            };
            scope["checkMailIsInList"] = function () {
                if (scope["form"]["sender_email"] && scope["form"]["recipient_address"]) {
                    ListChecker["get"]({
                        "hash": scope["form"]["recipient_address"],
                        "sender": scope["form"]["sender_email"]
                    }).$promise.then(function () {
                        scope["heIsInList"] = true;
                    }, function () {
                        scope["heIsInList"] = false;
                    });
                }
            };
            scope["sendForm"] = function () {
                if (ng.version["major"] >= 1 && ng.version["minor"] > 3) {
                    scope["form"]["csrfmiddlewaretoken"] =  cookies["get"]("csrftoken");
                } else {
                    scope["form"]["csrfmiddlewaretoken"] =  cookies["csrftoken"];
                }
                // WIP
                /*global console*/
                console.log(scope["form"]["csrfmiddlewaretoken"]);
            };
        }
    ]);
}(angular));
