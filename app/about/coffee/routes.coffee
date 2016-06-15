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
      "about", (
        "url": "/about"
        "templateUrl": "/about"
      )
    )
]
