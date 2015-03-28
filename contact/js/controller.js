/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.controller", [
        "hysoft.contact.resource"
    ]).controller("ContactController", [
        "$scope",
        "Contact",
        function (scope, Contact) {
            /*jslint sub: true*/

            // This trick is needed to avoid demangle
            // compression from closure compiler.
            scope["form"] = new Contact();
            scope["clearMailIsInList"] = function () {
                scope["heIsInList"] = undefined;
            };
            scope["checkMailIsInList"] = function () {
                if (scope["form"]["sender_email"] && scope["form"]["recipient_address"]) {
                    scope["form"]["$checkList"](
                        {"hash": scope["form"]["recipient_address"]}
                    ).then(function () {
                        scope["heIsInList"] = true;
                    }, function () {
                        scope["heIsInList"] = false;
                    });
                }
            };
        }
    ]);
}(angular));
