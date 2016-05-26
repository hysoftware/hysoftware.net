ng = angular

ng.module("hysoft.navbar.controller", [
  "ui.router"
]).controller("navbarController", [
  "$scope",
  "$state",
  "$window",
  "$rootElement",
  (scope, state, window, root) ->
    accept_transparent = [
      state.get "home"
      state.get "about_legal"
    ]
    isOnTitle = ->
      navbarHeigth = root.find("nav.main-menu").innerHeight()
      jumbotron = root.find(".ui-view .jumbotron").first()
      transparentEndPosition = 0
      try
        transparentEndPosition = (jumbotron.innerHeight() - navbarHeigth)
      catch
      window.scrollY < transparentEndPosition
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
