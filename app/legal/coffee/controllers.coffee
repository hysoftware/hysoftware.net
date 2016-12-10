angular.module("legal", [
  "common"
]).controller("legalCtrl", [
  "$scope", (scope) ->
    scope.model = {}
    scope.setCountry = (country) ->
      if country isnt '' and typeof country is "string"
        scope.model.country = country
])
