ng = angular

ng.module("hysoft.navbar.controller", [
]).controller("navbarController", [
  "$scope",
  "$window",
  (scope, window) ->
    navbarHeigth = 50
    scope.navbarClass =
      "on-title": window.scrollY < (window.innerHeight - navbarHeigth)
    window.onscroll = ->
      scope.$apply ->
        scope.navbarClass["on-title"] =
          window.scrollY < (window.innerHeight - navbarHeigth)
])
