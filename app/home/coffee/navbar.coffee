ng = angular

ng.module("hysoft.navbar.controller", [
  "ui.router"
]).controller("navbarController", [
  "$scope",
  "$state",
  "$window",
  (scope, state, window) ->
    navbarHeigth = 50
    accept_transparent = [
      state.get "home"
    ]
    isOnTitle = ->
      window.scrollY < (window.innerHeight - navbarHeigth)
    scope.navbarClass =
      "on-title": isOnTitle() and state.current
    window.onscroll = ->
      scope.$apply ->
        scope.navbarClass["on-title"] = isOnTitle() and
          accept_transparent.some (el) -> state.is el
    scope.$on "$stateChangeSuccess", ->
      scope.navbarClass["on-title"] = isOnTitle() and
        accept_transparent.some (el) -> state.is el
])
