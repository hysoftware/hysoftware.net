angular.module("hysoft.user.controllers", [
  "toaster"
  "hysoft.user.resources"
]).controller("loginController", [
  "$scope", "$timeout", "$window", "toaster", "UserSession",
  (scope, timeout, window, t, UserSession) ->
    scope.loginPageStyle =
      "height": window.innerHeight

    scope.isDirtyInvalid = (field) ->
      return field.$dirty and field.$invalid

    scope.model = new UserSession()
    scope.userStatus.$get().then (data) ->
      t.pop(
        "info", "Already logged in",
        "You are already logged into this website. To show this page, you
         must logout from this website."
      )
      scope.state.go "home"

    scope.send = ->
      delete scope.errors
      scope.model.$save().then(
        -> scope.userStatus.$get()
      ).then(
        -> timeout (-> scope.state.go "home"), 3000, false
      ).catch(
        (errors) ->
          scope.errors = errors
          scope.loginForm.$setPristine()
      )
      return

    window.onresize = ->
      scope.$apply ->
        scope.loginPageStyle.height = window.innerHeight
])
