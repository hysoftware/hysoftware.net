angular.module("common.ctrls", [
  "ngMaterial"
  "common.factories"
]).controller("dialogController", [
  "$scope", "$mdDialog", (scope, dialog) ->
    scope.dialog = dialog
]).controller("navBarCtrl", [
  "HeaderDetector", "$scope", "$window",
  (HeaderDetector, scope, wind) ->
    header = new HeaderDetector scope
    scope.navBarCls =
      "in": header.isWindowUnderHeader()
    wind.addEventListener "scroll", (->
      scope.$apply ->
        scope.navBarCls.in = header.isWindowUnderHeader()
    ), false
])
