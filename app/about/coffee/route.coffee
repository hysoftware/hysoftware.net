angular.module("hysoft.about", [
  "ui.router"
]).config [
  "$stateProvider", (state) ->
    state.state(
      "about_legal", (
        "url": "/about/legal"
        "templateUrl": "/about/legal"
      )
    ).state(
      "about_team", (
        "url": "/about"
        "templateUrl": "/about"
      )
    )
]
