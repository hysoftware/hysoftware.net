angular.module("hysoft.contact.resources", [
  "ngResource"
]).factory("Contact", [
  "$resource", "$timeout", (res, timeout) ->
    class ContactResource extends res "/contact"
      sendContact: (recaptchaToken, scope) ->
        delete @errors
        @["g-recaptcha-response"] = recaptchaToken
        @$save().then(
          =>
            @success = true
            timeout(
              (->
                scope.contact = new ContactResource()
                scope.contactForm.$setPristine()
              ), 5000, false
            )
        ).catch(
          (errors) =>
            @errors = errors
            scope.contactForm.$setPristine()
        ).finally ->
          grecaptcha.reset()
])
