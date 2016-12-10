angular.module("user.res", [
  "ngResource"
]).factory("ContactResource", [
  "$resource", (res) ->
    res "{{ url('user:contact') }}"
])
