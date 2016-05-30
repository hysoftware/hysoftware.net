ng = angular

ng.module("hysoft.navbar.controller", [
  "ui.router"
  "hysoft.user.resources"
]).controller("navbarController", [
  "$scope",
  "$state",
  "$window",
  "$rootElement",
  "UserSession"
  (scope, state, window, root, User) ->
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
    scope.logout = ->
      scope.userStatus.$delete()
      scope.userStatus = new User()
    window.onscroll = ->
      scope.$apply ->
        scope.navbarClass["on-title"] = isOnTitle() and
          accept_transparent.some (el) -> state.is el
    scope.$on "$stateChangeSuccess", ->
      scope.navbarClass["on-title"] = isOnTitle() and
        accept_transparent.some (el) -> state.is el
])
