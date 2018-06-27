/* eslint no-param-reassign: ["error", {
    "props": true,
    "ignorePropertyModificationsFor": ["http", "res", "root", "state", "wind"]
  }]
  */
/* eslint no-restricted-syntax: [
  "error", "FunctionExpression", "WithStatement",
] */
/* globals angular, Element */

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
  '$rootScope', '$window', (root, wind) => {
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
    // Full-screen functionality
    root.scrFullFillPrevState = {};
    root.screenFullFill =
      (id, scope, diffRate, minHeight = 0, minHeightRate = 1) => {
        root.scrFullFillPrevState[id] = {
          diffRate, minHeight, minHeightRate, scope,
        };
        const computedStyle = (
          minHeight instanceof Element
        ) ? wind.getComputedStyle(minHeight) : undefined;
        const minHeightPriv = (
          computedStyle ? parseInt(computedStyle.height.replace(/px/, ''), 10)
            : minHeight
        ) * minHeightRate;
        const expectedHeight = wind.innerHeight * (1 - diffRate);
        const height = (
          expectedHeight >= minHeightPriv
        ) ? expectedHeight : minHeightPriv;
        root.scrFullFillPrevState[id].height = height;
        return { height: `${height}px` };
      };
    root.particles = (tagId, param) => wind.particlesJS(tagId, param);
    wind.addEventListener('resize', () => {
      root.$apply(() => {
        for (const el in root.scrFullFillPrevState) {
          if ({}.hasOwnProperty.call(root.scrFullFillPrevState, el)) {
            ((elem, state) => {
              root.screenFullFill(
                elem, state.scope, state.diffRate,
                state.minHeight, state.minHeightRate
              );
              if (!state.scope.unregistDestroy) {
                state.scope.unregistDestroy =
                  state.scope.$on('$destroy', () => {
                    wind.removeEventListener('resize', wind);
                  });
              }
            })(el, root.scrFullFillPrevState[el]);
          }
        }
      });
    }, false);
    root.goto = (url) => { wind.location = url; };
  },
]);
