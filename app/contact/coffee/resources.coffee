angular.module("hysoft.contact.resources", [
  "ngResource"
]).factory("Contact", [
  "$resource", (res) ->
    res("/contact/:id", ("id": "@to"))
])
