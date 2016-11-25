angular.module("user.ctrls", [
  "ngMaterial"
]).controller("aboutCtrl", [
  "$element", "$scope", "$mdDialog", (elem, scope, dialog) ->
    scope.showStaff = (event, staffId) ->
      socialIcons =  elem[0].querySelector(
        ".member-card .social-links"
      ).children
      underSocial = false

      for socialIcon in socialIcons
        if socialIcon.contains(event.target) or socialIcon is event.target
          underSocial = true
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
  "$scope", (scope) ->
])
