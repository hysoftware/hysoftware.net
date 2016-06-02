ng = angular
ng.module("hysoft.home.controller", [
  "hysoft.common.form.validation"
]).controller(
  "homeController", [
    "$element", "$scope", "$window", "isDirtyInvalid",
    (element, scope, window, isDirtyInvalid) ->
      scope.contact = {}
      scope.isDirtyInvalid = isDirtyInvalid
      scope.titleStyle =
        "height": window.innerHeight

      scope.sendContact = ->
        scope.contact["g-recaptcha-response"] = element.find(
          "form#contactForm [name='g-recaptcha-response']"
        ).val()
        console.log scope.contact

      window.onresize = ->
        scope.$apply ->
          scope.titleStyle.height = window.innerHeight
])
