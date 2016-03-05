ng = angular
ng.module("hysoft.home.controller", [
]).controller(
  "homeController", [
    "$scope", "$window", (scope, window) ->
      scope.titleStyle =
        "height": window.innerHeight

      window.onresize = ->
        scope.$apply ->
          scope.titleStyle.height = window.innerHeight
])
