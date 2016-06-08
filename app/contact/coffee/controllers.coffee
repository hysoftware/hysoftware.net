angular.module("hysoft.contact.controllers", [
  "ui.router"
]).controller("contactController", [
  "$scope", "$stateParams", (scope, params) ->
    scope.contact = {}
    if params.id
      scope.contact.to = params.id
])
