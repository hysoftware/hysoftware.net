describe "Navbar tests", ->
  scope = undefined
  beforeEach ->
    module "hysoft.navbar.controller"
    module "hysoft.user.resources"
  beforeEach inject [
    "$controller", "$rootScope", "UserSession", (ctrl, root, User) ->
      scope = root.$new()
      scope.state = {
        "go": sinon.spy()
      }
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
  describe "Logout check (success)", ->
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
    it "User status should be empty.", inject [
      "$rootScope", (root)->
        expect(root.userStatus.email).is.empty
        expect(root.userStatus.firstname).is.empty
        expect(root.userStatus.lastname).is.empty
    ]
    it "scope.state.go should be called with 'home'", ->
      expect(scope.state.go.calledOnce).is.true
      expect(scope.state.go.calledWithExactly "home").is.true
  describe "Logout check (failure: 404)", ->
    beforeEach inject [
      "$httpBackend", (backend) ->
        backend.expectDELETE("/u/login").respond 404, ""
        scope.logout()
        backend.flush()
    ]
    afterEach inject [
      "$httpBackend", (backend) ->
        backend.verifyNoOutstandingExpectation()
        backend.verifyNoOutstandingRequest()
    ]
    it "User status shouldn't be empty.", ->
      expect(scope.userStatus.email).is.equal "test@example.com"
      expect(scope.userStatus.firstname).is.equal "test"
      expect(scope.userStatus.lastname).is.equal "example"
    it "scope.state.go shouldn't be called", ->
      expect(scope.state.go.notCalled).is.true
  describe "Logout check (failure: 500)", ->
    beforeEach inject [
      "$httpBackend", (backend) ->
        backend.expectDELETE("/u/login").respond 500, ""
        scope.logout()
        backend.flush()
    ]
    afterEach inject [
      "$httpBackend", (backend) ->
        backend.verifyNoOutstandingExpectation()
        backend.verifyNoOutstandingRequest()
    ]
    it "User status shouldn't be empty.", ->
      expect(scope.userStatus.email).is.equal "test@example.com"
      expect(scope.userStatus.firstname).is.equal "test"
      expect(scope.userStatus.lastname).is.equal "example"
    it "scope.state.go shouldn't be called", ->
      expect(scope.state.go.notCalled).is.true
