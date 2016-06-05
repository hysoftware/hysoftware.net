angular.module("hysoft.user.route", [
  "ui.router"
  "hysoft.user.controllers"
]).config([
  "$stateProvider", (state) ->
    state.state(
      "login", (
        "url": "/login"
        "templateUrl": "/u/login"
        "controller": "loginController"
      )
    )
])
