angular.module("common", [
  "ngMaterial"
  "common.factories"
]).config([
  "$httpProvider", (http) ->
    http.defaults.xsrfCookieName = "csrftoken"
    http.defaults.xsrfHeaderName = "X-CSRFToken"
]).run([
  "$rootScope", "$window", (root, wind) ->
    # Form / Model Related Stuff
    root.sendBtnCap = (form) ->
      form.$submitted || form.$invalid || form.$pristine
    root.unsetSubmitOnChange = (model, form) ->
      unwatch = root.$watch (-> model), (->
        unwatch()
        if form.$submitted
          form.$setPristine()
      ), true
    root.isDirtyInvalid = (fld) ->
      return fld.$dirty and fld.$invalid
    # root.fillModel = (scope, target_elem) ->
    #   for elem in target_elem.querySelectorAll "[data-ng-model][value]"
    #     do (elem) ->
    #       val = elem.value
    #       date = new Date(val)
    #       scope.$eval "#{elem.dataset.ngModel} = val", (
    #         val: (if isNaN date.getTime() then val else date)
    #       )
    #   for elem in target_elem.querySelectorAll(
    #     "[type=\"checkbox\"][data-ng-model]"
    #   )
    #     do (elem) ->
    #       scope.$eval "#{elem.dataset.ngModel} = val", (
    #         val: elem.getAttribute("checked") is "checked"
    #       )

    # Full-screen functionality
    root.scrFullFillPrevState = {}
    root.screenFullFill = (
      id, scope, diffRate, minHeight=0, minHeightRate=1
    ) ->
      root.scrFullFillPrevState[id]=
        "heightDiffRate": diffRate
        "minHeight": minHeight
        "minHeightRate": minHeightRate
        "scope": scope
      computedStyle = undefined
      if minHeight instanceof Element
        computedStyle = wind.getComputedStyle(minHeight)
      _minHeight = if computedStyle then parseInt(
        computedStyle.height.replace(/px/, "")
      ) else minHeight
      _minHeight = _minHeight * minHeightRate
      expected_height = wind.innerHeight * (1 - diffRate)
      height = undefined
      if expected_height >= _minHeight
        height = expected_height
      else
        height = _minHeight
      root.scrFullFillPrevState[id].height = height
      "height": "#{height}px"
    wind.addEventListener "resize", (->
      handler = @
      root.$apply ->
        for elem, state of root.scrFullFillPrevState
          do (elem, state) ->
            root.screenFullFill(
              elem, state.scope, state.heightDiffRate,
              state.minHeight, state.minHeightRate
            )
            if state.scope.unregistDestroy is undefined
              state.scope.unregistDestroy = state.scope.$on("$destroy", ->
                wind.removeEventListener("resize", handler)
              )
    ), false
]).controller("navBarCtrl", [
  "HeaderDetector", "$scope", "$window",
  (HeaderDetector, scope, wind) ->
    header = new HeaderDetector scope
    scope.navBarCls =
      "out": not header.isWindowUnderHeader()
    wind.addEventListener "scroll", (->
      scope.$apply ->
        scope.navBarCls.out = not header.isWindowUnderHeader()
    ), false
])
