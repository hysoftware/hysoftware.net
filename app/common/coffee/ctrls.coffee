angular.module("common.ctrls", [
  "ngMaterial"
]).controller("dialogController", [
  "$scope", "$mdDialog", (scope, dialog) ->
    scope.dialog = dialog
])
