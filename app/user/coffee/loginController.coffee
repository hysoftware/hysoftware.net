angular.module("hysoft.user.controllers", [
  "hysoft.user.resources"
]).controller("loginController", [
  "$scope", "$timeout", "$window", "UserSession",
  (scope, timeout, window, UserSession) ->
    scope.loginPageStyle =
      "height": window.innerHeight

    scope.isDirtyInvalid = (field) ->
      return field.$dirty and field.$invalid

    scope.model = new UserSession()

    scope.send = ->
      delete scope.errors
      scope.model.$save().then(
        -> scope.userStatus.$get()
      ).then(
        -> timeout(-> scope.state.go "home", 2500)
      ).catch (errors) ->
        scope.errors = errors
      return

    window.onresize = ->
      scope.$apply ->
        scope.loginPageStyle.height = window.innerHeight
])
