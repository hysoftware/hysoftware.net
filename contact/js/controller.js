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
        "$stateParams",
        "Contact",
        "ListChecker",
        function (scope, stateParams, Contact, ListChecker) {
            /*jslint sub: true*/

            // This trick is needed to avoid demangle
            // compression from closure compiler.
            scope["form"] = new Contact();
            if (stateParams["dev"]) {
                scope["form"]["recipient_address"] = stateParams["dev"];
            }
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
    ]).filter("verificationErrorFilter", function () {
        return function (input) {
            var map = {
                "frontend": "Frontend (Probably, your email)",
                "backend": "Backend",
                "email": "Your email"
            };
            return map[input];
        };
    }).controller("VerificationController", [
        "$scope",
        "$stateParams",
        "Verify",
        function (scope, params, Verify) {
            /*jslint sub: true*/
            scope["form"] = new Verify({"token": params["token"]});
            scope["send"] = function () {
                scope["error"] = {};
                scope["form"]["$save"]()["catch"](function (errData) {
                    var addErrorWithoutData = function () {
                        if (errData["status"] < 500) {
                            scope["error"] = {
                                "error": errData["status"],
                                "frontend": [
                                    "Not critical, but please re-type email address used contact form..."
                                ]
                            };
                        } else {
                            scope["error"] = {
                                "error": errData["status"] || 500,
                                "backend": "Backend doesn't seem to be working"
                            };
                        }
                    }, key;
                    if (errData["status"] < 500) {
                        scope["form"] = new Verify(
                            {"token": params["token"]}
                        );
                        scope["emailForm"]["$setPristine"]();
                    }
                    if (errData["data"]) {
                        if (errData["data"]["error"] !== undefined) {
                            scope["error"] = errData["data"];
                        } else {
                            scope["error"] = {
                                "error": errData["status"]
                            };
                            if (typeof errData["data"] === "object") {
                                for (key in errData["data"]) {
                                    if (errData["data"].hasOwnProperty(key)) {
                                        scope["error"][key] = errData["data"][key];
                                    }
                                }
                            } else {
                                addErrorWithoutData();
                            }
                        }
                    } else {
                        addErrorWithoutData();
                    }
                });
            };
        }
    ]);
}(angular));
