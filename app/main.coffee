angular.module("hysoft", [
  "ui.router"
  "hysoft.home"
  "hysoft.navbar.controller"
]).config([
  "$urlRouterProvider", "$httpProvider", (url, http) ->
    url.otherwise (injector, to) ->
      if not to.url()
        to.path "/"
      else
        to.path "/oops"
    http.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest"
    http.defaults.xsrfCookieName = http.defaults.xsrfHeaderName = "X-CSRFToken"
])
