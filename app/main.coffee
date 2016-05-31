angular.module("hysoft", [
  "ui.router"
  "hysoft.about"
  "hysoft.home"
  "hysoft.navbar.controller",
  "hysoft.user.route",
  "hysoft.user.resources"
]).config([
  "$urlRouterProvider", "$httpProvider", (url, http) ->
    url.otherwise (injector, to) ->
      if not to.url()
        to.path "/"
      else
        to.path "/oops"
    http.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest"
    http.defaults.xsrfCookieName = http.defaults.xsrfHeaderName = "X-CSRFToken"
]).run([
  "$rootScope", "$state", "UserSession", (rootScope, state, User) ->
    rootScope.state = state
    rootScope.userStatus = User.get()
    rootScope.angular = angular
])
