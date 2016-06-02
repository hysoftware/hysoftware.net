angular.module("hysoft.home.controller", [
  "hysoft.common.form.validation"
  "hysoft.contact.resources"
]).controller(
  "homeController", [
    "$element", "$scope", "$window", "Contact", "isDirtyInvalid",
    (element, scope, window, Contact, isDirtyInvalid) ->
      scope.contact = new Contact()
      scope.isDirtyInvalid = isDirtyInvalid
      scope.titleStyle =
        "height": window.innerHeight
      scope.contactErrors = {}

      scope.sendContact = ->
        scope.contactErrors = {}
        scope.contact["g-recaptcha-response"] = element.find(
          "form#contactForm [name='g-recaptcha-response']"
        ).val()
        scope.contact.$save().then(
          -> scope.contact = new Contact()
        ).catch(
          (errors) ->
            scope.contactErrors = errors
            scope.contactForm.$setPristine()
        )

      window.onresize = ->
        scope.$apply ->
          scope.titleStyle.height = window.innerHeight
])
