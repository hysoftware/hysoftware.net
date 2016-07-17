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
  (rootScope, scope, state, win, root, t, User) ->
    accept_transparent = [
      state.get "home"
      state.get "about_legal"
      state.get "about"
      state.get "contact"
      state.get "contact_id"
    ]
    isOnTitle = ->
      navbarHeigth = root.find("nav.main-menu").innerHeight()
      jumbotron = root.find(".ui-view .jumbotron").first()
      transparentEndPosition = 0
      try
        transparentEndPosition = (jumbotron.innerHeight() - navbarHeigth)
      catch
      win.scrollY < transparentEndPosition
    scope.navbarClass =
      "on-title": true
    scope.logout = ->
      scope.userStatus.$delete().then(->
        t.pop(
          "success", "Goodbye! #{scope.userStatus.firstname}!",
          "Have a nice day."
        )
        rootScope.userStatus = new User()
        scope.state.go "home"
      )
    root.load ->
      scope.$apply ->
        scope.navbarClass["on-title"] = isOnTitle() and
          accept_transparent.some (el) -> state.is el
    win.addEventListener "scroll", ->
      scope.$apply ->
        scope.navbarClass["on-title"] = isOnTitle() and
          accept_transparent.some (el) -> state.is el
])
