angular.module("hysoft.contact.controllers", [
  "ui.router"
  "hysoft.common.form.validation"
  "hysoft.contact.resources"
]).controller("contactController", [
  "Contact", "isDirtyInvalid", "$element", "$scope", "$stateParams",
  (Contact, isDirtyInvalid, element, scope, params) ->
    scope.contact = new Contact()
    scope.isDirtyInvalid = isDirtyInvalid
    if params.id
      scope.contact.to = params.id
    scope.sendContact = ->
      scope.contact.sendContact(
        element.find(
          "form#contactForm [name='g-recaptcha-response']"
        ).val(), scope
      )
      return
])
