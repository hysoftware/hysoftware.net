angular.module("hysoft.user.controllers", [
]).controller("loginController", [
  "$scope", "$window", (scope, window) ->
    scope.loginPageStyle =
      "height": window.innerHeight

    scope.isDirtyInvalid = (field) ->
      return field.$dirty and field.$invalid

    scope.model = {}

    scope.send = ->
      console.log scope.model

    window.onresize = ->
      scope.$apply ->
        scope.loginPageStyle.height = window.innerHeight
])
