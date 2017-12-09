/* global angular, grecaptcha */
/* eslint no-param-reassign: ["error", {
    "props": true,
    "ignorePropertyModificationsFor": ["scope", "wind"]
  }]
  */
/* eslint no-restricted-syntax: [
  "error", "FunctionExpression", "WithStatement",
] */

import './res.es6';

export default angular.module('user.ctrls', [
  'user.res',
]).controller('aboutCtrl', [
  '$element', '$scope', '$mdDialog', (elem, scope, dialog) => {
    scope.showStaff = (event, staffId) => {
      const socialIconsParents = elem[0].querySelectorAll(
        '.member-card .social-links'
      );
      let underSocial = false;
      for (const socialIcons of socialIconsParents) {
        for (const socialIcon of socialIcons.children) {
          if (
            socialIcon.contains(event.target) ||
            socialIcon === event.target
          ) {
            underSocial = true;
            break;
          }
        }
        if (underSocial) { break; }
      }
      if (!underSocial) {
        dialog.show({
          targetEvent: event,
          controller: 'staffCtrl',
          templateUrl: `{{ url(\
              "user:staff",\
              kwargs={"info_id": "00000000-0000-0000-0000-000000000000"}\
          ).replace("00000000-0000-0000-0000-000000000000", "")}}${staffId}`,
          clickOutsideToClose: true,
        });
      }
    };
  },
]).controller('staffCtrl', [
  '$scope', '$window', (scope, wind) => {
    scope.state = {}
    scope.open = (url) => {
      wind.open(url);
      return true;
    };
  },
]).controller('contactCtrl', [
  'ContactResource', '$scope', '$timeout', '$window',
  (Contact, scope, timeout, wind) => {
    scope.model = new Contact();
    scope.sent = false;
    scope.send = (formName) => {
      scope.sent = false;
      scope.formName = formName;
      if (scope.errors) {
        delete scope.errors;
      }
      grecaptcha.execute();
    };
    wind.recaptchaCallback = (token) => {
      scope.model['g-recaptcha-response'] = token;
      scope.model.$save().then(
        () => { scope.sent = true; }
      ).catch((err) => {
        scope.errors = err;
        grecaptcha.reset();
        timeout(() => { scope[scope.formName].$setPristine(); }, 3000);
      });
    };
  },
]);
