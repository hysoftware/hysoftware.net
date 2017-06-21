/* eslint no-param-reassign: ["error", {
    "props": true,
    "ignorePropertyModificationsFor": ["scope"]
  }]
  */
/* global angular */

export default angular.module('legal', [
  'common',
]).controller('legalCtrl', [
  '$scope', (scope) => {
    scope.model = {};
    scope.setCountry = (country) => {
      if (country !== '' && typeof country === 'string') {
        scope.model.country = country;
      }
    };
  },
]);
