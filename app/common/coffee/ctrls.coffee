angular.module("common.ctrls", [
  "ngMaterial"
]).controller("dialogHeaderController", [
  "$scope", "$mdDialog", (scope, dialog) ->
    scope.dialog = dialog
])
