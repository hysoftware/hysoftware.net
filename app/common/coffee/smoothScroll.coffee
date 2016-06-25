angular.module("smoothScroll", [
]).factory("scrollTo", [
  -> (target, easing, duration) ->
    angular.element("html, body").animate(
      "scrollTop": angular.element(target).offset().top - 50
      "easing": easing or "swing"
      "duration": duration or 400
    )
    return
])
