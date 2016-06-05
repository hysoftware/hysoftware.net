ng = angular

ng.module("hysoft.navbar.controller", [
  "ui.router"
  "toaster"
  "hysoft.user.resources"
]).controller("navbarController", [
  "$rootScope",
  "$scope",
  "$state",
  "$window",
  "$rootElement",
  "toaster",
  "UserSession"
  (rootScope, scope, state, window, root, t, User) ->
    accept_transparent = [
      state.get "home"
      state.get "about_legal"
      state.get "about"
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
      scope.userStatus.$delete().then(->
        t.pop(
          "success", "Goodbye! #{scope.userStatus.firstname}!",
          "Have a nice day."
        )
        rootScope.userStatus = new User()
        scope.state.go "home"
      )
    window.onscroll = ->
      scope.$apply ->
        scope.navbarClass["on-title"] = isOnTitle() and
          accept_transparent.some (el) -> state.is el
    scope.$on "$stateChangeSuccess", ->
      scope.navbarClass["on-title"] = isOnTitle() and
        accept_transparent.some (el) -> state.is el
])
