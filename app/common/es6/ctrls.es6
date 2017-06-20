/* globals angular */
import './factories.es6';

export default angular.module('common.ctrls', [
  'ngMaterial',
  'common.factories',
]).controller('dialogController', [
  '$scope', '$mdDialog', (scope, dialog) => {
    scope.dialog = dialog;
  },
]).controller('navBarCtrl', [
  'HeaderDetector', '$mdSidenav', '$scope', '$window',
  (HeaderDetector, sidenav, scope, wind) => {
    const header = new HeaderDetector(scope);
    scope.sideNav = sidenav;
    scope.navBarCls = { in: header.isWindowUnderHeader() };
    wind.addEventListener('scroll', () => {
      scope.$apply(() => {
        scope.navBarCls.in = header.isWindowUnderHeader();
      });
    }, false);
  },
]);
