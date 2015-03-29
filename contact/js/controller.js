/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.controller", [
        "ngCookies",
        "hysoft.contact.resource"
    ]).controller("ContactController", [
        "$scope",
        "Contact",
        "ListChecker",
        function (scope, Contact, ListChecker) {
            /*jslint sub: true*/

            // This trick is needed to avoid demangle
            // compression from closure compiler.
            scope["form"] = new Contact();
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
                scope["form"]["$save"]();
            };
        }
    ]);
}(angular));
