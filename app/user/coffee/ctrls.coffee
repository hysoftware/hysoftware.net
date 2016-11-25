angular.module("user.ctrls", [
  "ngMaterial"
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
  "$scope", (scope) -> undefined
])
