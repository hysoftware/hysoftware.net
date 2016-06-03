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
        delete scope.contactErrors
        scope.contact["g-recaptcha-response"] = element.find(
          "form#contactForm [name='g-recaptcha-response']"
        ).val()
        scope.contact.$save().then(
          -> timeout(
            (->
              scope.contact = new Contact()
              scope.contactForm.$setPristine()
              try
                grecaptcha.reset()
              catch
            ), 5000, false
          )
        ).catch(
          (errors) ->
            scope.contactErrors = errors
            scope.contactForm.$setPristine()
        )

      window.onresize = ->
        scope.$apply ->
          scope.titleStyle.height = window.innerHeight
])
