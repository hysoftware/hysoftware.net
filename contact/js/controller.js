/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.controller", [
        "ui.router",
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
    ]).controller("VerificationController", [
        "$scope",
        "$stateParams",
        "Verify",
        function (scope, params, Verify) {
            /*jslint sub: true*/
            scope["form"] = new Verify({"token": params["token"]});
            scope["send"] = function () {
                scope["form"]["$save"]()["catch"](function (errData) {
                    if (errData["data"]) {
                        var key;
                        if (errData["data"]["error"]) {
                            scope["error"] = errData["data"];
                        } else {
                            scope["error"] = {
                                "error": errData["status"]
                            };
                            for (key in errData["data"]) {
                                if (errData["data"].hasOwnProperty(key)) {
                                    scope["error"][key] = errData["data"][key];
                                }
                            }
                        }
                    } else {
                        scope["error"] = {
                            "error": errData["status"] || 500,
                            "backend": "Backend doesn't seem to be working"
                        };
                    }
                });
            };
        }
    ]);
}(angular));
