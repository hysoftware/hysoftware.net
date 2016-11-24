angular.module("user.ctrls", [
  "ngMaterial"
]).controller("aboutCtrl", [
  "$scope", "$mdDialog", (scope, dialog) ->
    scope.showStaff = (staffId) ->
      dialog.show(
        "controller": "staffCtrl"
        "templateUrl": "{{
          url(
            'user:staff',
            kwargs={'info_id': '00000000-0000-0000-0000-000000000000'}
          ).replace('00000000-0000-0000-0000-000000000000', '')
        }}#{staffId}"
      )
]).controller("staffCtrl", [
  "$scope", (scope) ->
])
