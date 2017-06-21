/* globals angular */
export default angular.module('common.factories', [
]).factory('HeaderDetector', [
  '$rootElement', '$window', (rootElem, wind) => class HeaderDetector {
    constructor(scope) {
      this.scope = scope;
      this.header = rootElem[0].querySelector('header');
    }
    height() {
      return parseFloat(
        wind.getComputedStyle(this.header).height.replace(/[^0-9.]/g, '')
      );
    }
    isWindowUnderHeader() {
      if (this.scope.enableTransparentMenu) {
        const offsetY = this.header.offsetTop;
        return offsetY <= wind.scrollY &&
          wind.scrollY <= ((offsetY + this.height()) - 45);
      }
      return true;
    }
  }]);
