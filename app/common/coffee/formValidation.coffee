angular.module("hysoft.common.form.validation", [
]).factory("isDirtyInvalid", [
  -> (field) -> !field or (field.$dirty and field.$invalid)
])
