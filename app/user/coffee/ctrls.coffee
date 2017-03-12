angular.module("user.ctrls", [
  "user.res"
]).controller("aboutCtrl", [
  "$element", "$scope", "$mdDialog", (elem, scope, dialog) ->
    scope.showStaff = (event, staffId) ->
      socialIconsParents =  elem[0].querySelectorAll(
        ".member-card .social-links"
      )
      underSocial = false

      for socialIcons in socialIconsParents
        for socialIcon in socialIcons.children
          if socialIcon.contains(event.target) or socialIcon is event.target
            underSocial = true
            break
        if underSocial
          break

      if not underSocial
        dialog.show(
          "targetEvent": event
          "controller": "staffCtrl"
          "templateUrl": "{{
            url(
              'user:staff',
              kwargs={'info_id': '00000000-0000-0000-0000-000000000000'}
            ).replace('00000000-0000-0000-0000-000000000000', '')
          }}#{staffId}",
          "clickOutsideToClose": true
        )
]).controller("staffCtrl", [
  "$scope", "$window", (scope, wind) ->
    scope.open = (url) ->
      wind.open url
      return true
]).controller("contactCtrl", [
  "ContactResource", "$scope", "$timeout", "$window"
  (Contact, scope, timeout, wind) ->
    scope.model = new Contact()
    scope.sent = false
    scope.send = (form_name)->
      scope.sent = false
      if scope.errors
        delete scope.errors
      grecaptcha.execute()
    wind.recaptchaCallback = (token) ->
      scope.model["g-recaptcha-response"] = token
      scope.model.$save().then(
        -> scope.sent = true
      ).catch(
        (err) ->
          scope.errors = err
          grecaptcha.reset()
          timeout (-> scope[form_name].$setPristine()), 3000
      )
])

# window.recaptchaCallback = (token)->
#   angular.element(
#     document.querySelector "[data-ng-controller='contactCtrl']"
#   ).scope().afterBotCheck token
