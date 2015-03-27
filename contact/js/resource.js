/*global angular*/
(function (ng) {
    "use strict";
    ng.module("hysoft.contact.resource", [
        "ngResource"
    ]).factory("DeveloperAddress", ["$resource", function (res) {
        return res("contact/address", {}, {
            "get": {"method": "GET", "isArray": true}
        });
    }]);
}(angular));
