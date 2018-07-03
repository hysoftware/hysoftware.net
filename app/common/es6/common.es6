/* eslint no-param-reassign: ["error", {
    "props": true,
    "ignorePropertyModificationsFor": ["http", "res", "root", "state", "wind"]
  }]
  */
/* eslint no-restricted-syntax: [
  "error", "FunctionExpression", "WithStatement",
] */
/* globals angular */

import './ctrls.es6';

export default angular.module('common', [
  'ngMaterial',
  'ngResource',
  'ngMessages',
  'common.ctrls',
]).config([
  '$httpProvider', '$resourceProvider', (http, res) => {
    http.defaults.xsrfCookieName = 'csrftoken';
    http.defaults.xsrfHeaderName = 'X-CSRFToken';
    res.defaults.stripTrailingSlashes = false;
  },
]).run([
  '$document', '$rootScope', '$timeout', '$window',
  (doc, root, timeout, wind) => {
    // Form / Model Related Stuff
    root.sendBtnCap = (form) => {
      const ret = form.$submitted || form.$invalid || form.$pristine;
      return ret;
    };
    root.unsetSubmitOnChange = (model, form) => {
      const unwatch = root.$watch(() => model, () => {
        unwatch();
        if (form.$submitted) {
          form.$setPristine();
        }
      }, true);
    };
    root.isDirtyInvalid = (fld) => {
      const isDirty = fld.$dirty && fld.$invalid;
      return isDirty;
    };
    root.particles = (tagId, param) => {
      const unwatch = root.$watch(
        () => doc[0].styleSheets,
        (data) => {
          if (data.length > 0) {
            unwatch();
            wind.particlesJS(tagId, param);
          }
        }
      );
    };
    root.goto = (url) => { wind.location = url; };
  },
]);
