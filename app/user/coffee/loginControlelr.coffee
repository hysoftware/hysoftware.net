angular.module("hysoft.user.controllers", [
]).controller("loginController", [
  "$scope", "$window", (scope, window) ->
    scope.loginPageStyle =
      "height": window.innerHeight

    window.onresize = ->
      scope.$apply ->
        scope.loginPageStyle.height = window.innerHeight
])
