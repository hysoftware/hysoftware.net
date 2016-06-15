angular.module("hysoft.home.controller", [
  "hysoft.common.form.validation"
  "hysoft.contact.resources"
]).controller(
  "homeController", [
    "$element", "$scope", "$timeout", "$window", "Contact", "isDirtyInvalid",
    (element, scope, timeout, window, Contact, isDirtyInvalid) ->
      scope.contact = new Contact()
      scope.isDirtyInvalid = isDirtyInvalid
      scope.titleStyle =
        "height": window.innerHeight

      scope.sendContact = ->
        scope.contact.sendContact(
          element.find(
            "form#contactForm [name='g-recaptcha-response']"
          ).val(), scope
        )
        return

      window.onresize = ->
        scope.$apply ->
          scope.titleStyle.height = window.innerHeight
])
