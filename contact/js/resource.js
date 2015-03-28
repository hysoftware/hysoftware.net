/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.resource", [
        "ngResource"
    ]).factory("Contact", ["$resource", function (res) {
        return res("contact/:hash", {
            "hash": ""
        }, {
            "checkList": {
                "url": "/contact/check/:hash",
                "method": "GET"
            }
        });
    }]);
}(angular));
