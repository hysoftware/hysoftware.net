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
        delete scope.contactSuccess
        scope.contact["g-recaptcha-response"] = element.find(
          "form#contactForm [name='g-recaptcha-response']"
        ).val()
        console.log scope.contact
        scope.contact.$save().then(
          ->
            scope.contactSuccess = true
            timeout(
              (->
                scope.contact = new Contact()
                scope.contactForm.$setPristine()
              ), 5000, false
            )
        ).catch(
          (errors) ->
            scope.contactErrors = errors
            scope.contactForm.$setPristine()
        ).finally ->
          try
            grecaptcha.reset()
          catch

      window.onresize = ->
        scope.$apply ->
          scope.titleStyle.height = window.innerHeight
])
