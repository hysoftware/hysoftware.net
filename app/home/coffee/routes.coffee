ng = angular
ng.module("hysoft.home", [
  "ngAnimate"
  "ui.router"
  "toaster"
  "hysoft.home.controller"
]).config([
  "$stateProvider", (stateProvider) ->
    stateProvider.state(
      "home", (
        "url": "/"
        "controller": "homeController",
        "templateUrl": "/home"
      )
    ).state(
      "oops",
      "url": "/oops"
    )
])
