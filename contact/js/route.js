/*global angular*/
(function (a) {
    "use strict";
    a.module("hysoft.contact.route", [
        "ui.router"
    ]).config(["$stateProvider", function (stateProvider) {
        stateProvider.state(
            "contact",
            {
                "url": "/contact",
                "templateUrl": "contact"
            }
        );
    }]);
}(angular));
