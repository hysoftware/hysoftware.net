angular.module("hysoft.home.controller", [
  "smoothScroll"
  "hysoft.common.form.validation"
  "hysoft.contact.resources"
]).controller(
  "homeController", [
    "$element", "$scope", "$timeout", "$window", "Contact", "isDirtyInvalid",
    "scrollTo"
    (element, scope, timeout, window, Contact, isDirtyInvalid, scrollTo) ->
      scope.contact = new Contact()
      scope.isDirtyInvalid = isDirtyInvalid
      scope.titleStyle =
        "height": window.innerHeight
      scope.scrollTo = scrollTo

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
