angular.module("hysoft.contact.routes", [
  "ui.router"
  "hysoft.contact.controllers"
]).config([
  "$stateProvider", (state) ->
    state.state("contact_id", (
      "url": "/contact/:id"
      "templateUrl": (params) -> "/contact/#{params.id}"
      "controller": "contactController"
    )).state("contact", (
      "url": "/contact",
      "templateUrl": "/contact"
      "controller": "contactController"
    ))
])
