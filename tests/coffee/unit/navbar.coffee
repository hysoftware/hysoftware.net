describe "Navbar tests", ->
  scope = undefined
  beforeEach ->
    module "hysoft.navbar.controller"
    module "hysoft.user.resources"
  beforeEach inject [
    "$controller", "$rootScope", "UserSession", (ctrl, root, User) ->
      scope = root.$new()
      scope.userStatus = new User({
        "firstname": "test",
        "lastname": "example",
        "email": "test@example.com"
      })
      ctrl(
        "navbarController", (
          "$scope": scope
        )
      )
  ]
  describe "Logout check", ->
    beforeEach inject [
      "$httpBackend", (backend) ->
        backend.expectDELETE("/u/login").respond 200, ""
        scope.logout()
        backend.flush()
    ]
    afterEach inject [
      "$httpBackend", (backend) ->
        backend.verifyNoOutstandingExpectation()
        backend.verifyNoOutstandingRequest()
    ]
    it "User status should be empty.", ->
      expect(scope.userStatus.email).is.empty
      expect(scope.userStatus.firstname).is.empty
      expect(scope.userStatus.lastname).is.empty
