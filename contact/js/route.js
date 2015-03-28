/*global angular*/
(function (a) {
    "use strict";
    a.module("hysoft.contact.route", [
        "ui.router",
        "hysoft.contact.controller"
    ]).config(["$stateProvider", function (stateProvider) {
        stateProvider.state(
            "contact",
            {
                "url": "/contact",
                "templateUrl": "/contact",
                "controller": "ContactController"
            }
        ).state(
            "contact_slash",
            {
                "url": "/contact/",
                "templateUrl": "/contact",
                "controller": "ContactController"
            }
        ).state(
            "contact_specific",
            {
                "url": "/contact/{dev:[a-f,0-9]{40}}",
                "templateUrl": function (params) {
                    /*jslint sub: true*/
                    return "/contact/" + params["dev"];
                }
            }
        );
    }]);
}(angular));
