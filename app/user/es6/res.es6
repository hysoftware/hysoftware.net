/* global angular */

export default angular.module('user.res', [
  'ngResource',
]).factory('ContactResource', [
  '$resource', (res) => {
    const ret = res('{{ url("user:contact") }}');
    return ret;
  },
]);
