angular.module(
  "hysoft.user.resources", ["ngResource"]
).factory("UserSession", [
  "$resource", (res) -> res "/u/login", {}, (
    "get":
      "url": "/u/login/status"
  )
])
