ng = angular
ng.module("hysoft.home.controller", [
]).controller(
  "homeController", [
    "$element", "$scope", "$window", (element, scope, window) ->
      scope.contact = {}
      scope.titleStyle =
        "height": window.innerHeight

      scope.sendContact = ->
        scope.contact["g-recaptcha-response"] = element.find(
          "form#contactForm *[name='g-recaptcha-response']"
        ).val()
        scope.contact

      window.onresize = ->
        scope.$apply ->
          scope.titleStyle.height = window.innerHeight
])
