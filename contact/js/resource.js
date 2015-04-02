/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.resource", [
        "ngResource"
    ]).factory("Contact", ["$resource", function (res) {
        return res("/contact/:hash", {
            "hash": "@recipient_address"
        });
    }]).factory("ListChecker", ["$resource", function (res) {
        return res("/contact/check/:hash", {
            "hash": "@recipient_address"
        });
    }]).factory("Verify", ["$resource", function (res) {
        return res("/contact/verify/:token", {
            "token": "@token"
        });
    }]);
}(angular));
