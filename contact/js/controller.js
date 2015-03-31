/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.controller", [
        "ngCookies",
        "hysoft.contact.resource"
    ]).filter("errorConversion", [function () {
        return function (input) {
            var conversionMap = {
                "sender_name": "Your Name",
                "sender_email": "Your Email Address",
                "recipient_address": "Hysoft person",
                "message": "Your message",
                "backend": "Backend Program"
            };
            return conversionMap[input] || input;
        };
    }]).controller("ContactController", [
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
            scope["error"] = {};
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
                scope["form"]["$save"]().then(function () {
                    scope["contactForm"]["$setPristine"]();
                    scope["contactForm"]["$setSubmitted"]();
                }, function (data) {
                    if (!data["data"]) {
                        scope["error"] = {
                            "error": 500,
                            "backend": "Backend seems to be down"
                        };
                    } else {
                        scope["error"] = data["data"];
                    }
                });
            };
        }
    ]);
}(angular));
