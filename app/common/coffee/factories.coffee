angular.module("common.factories", [
]).factory("HeaderDetector", [
  "$rootElement", "$window", (rootElem, wind) ->
    class HeaderDetector
      constructor: (@scope) -> @header = rootElem[0].querySelector "header"
      height: ->
        parseFloat wind.getComputedStyle(@header).height.replace(/[^0-9.]/g, "")
      isWindowUnderHeader: ->
        if @scope.enableTransparentMenu
          offsetY = @header.offsetTop
          return offsetY <= wind.scrollY <= (offsetY + @height() - 45)
        else return true
])
