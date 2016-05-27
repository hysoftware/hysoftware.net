angular.module("hysoft.user.controllers", [
  "hysoft.user.resources"
]).controller("loginController", [
  "$scope", "$window", "UserSession", (scope, window, UserSession) ->
    scope.loginPageStyle =
      "height": window.innerHeight

    scope.isDirtyInvalid = (field) ->
      return field.$dirty and field.$invalid

    scope.model = new UserSession()

    scope.send = ->
      scope.model.$save()

    window.onresize = ->
      scope.$apply ->
        scope.loginPageStyle.height = window.innerHeight
])
