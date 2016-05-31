describe "Login Controller Tests", ->
  controller = undefined
  scope = undefined
  beforeEach ->
    module "ngMock"
    module "hysoft.user.controllers"

  describe "Logged in", ->
    beforeEach inject [
      "$httpBackend", "$rootScope", "$controller", "UserSession",
      (http, root, ctrl, User) ->
        http.expectGET("/u/login/status").respond 200, ""
        scope = root.$new()
        scope.userStatus = new User();
        scope.state = {"go": sinon.spy()}
        controller = ctrl "loginController", (
          "$scope": scope
        )
        http.flush()
        http.verifyNoOutstandingExpectation()
        http.verifyNoOutstandingRequest()
    ]
    it "scope.state.go 'home' should be called at this time.", ->
      expect(scope.state.go.calledOnce).is.true
      expect(scope.state.go.calledWithExactly "home").is.true
  describe "Not logged in", ->
    beforeEach inject [
      "$httpBackend", "$rootScope", "$controller", "UserSession",
      (http, root, ctrl, User) ->
        http.expectGET("/u/login/status").respond 401, ""
        scope = root.$new()
        scope.userStatus = new User();
        scope.loginForm =
          "$setPristine": sinon.spy();
        scope.state = {"go": sinon.spy()}
        controller = ctrl "loginController", (
          "$scope": scope
        )
        http.flush()
        http.verifyNoOutstandingExpectation()
        http.verifyNoOutstandingRequest()
    ]
    it "scope.state.go 'home' shouldn't be called at this time.", ->
      expect(scope.state.go.called).is.false
    describe "isDirtyInvalid check", ->
      testCases = [
        ("$invalid": true, "$dirty": true, "expected": true),
        ("$invalid": false, "$dirty": true, "expected": false),
        ("$invalid": true, "$dirty": false, "expected": false),
        ("$invalid": false, "$dirty": false, "expected": false)
      ]
      for testData in testCases
        do (testData) ->
          describe "When Invalid = #{testData.$invalid} and
                   Dirty = #{testData.$dirty}", ->
            it "Should return #{testData.expected}", ->
              result = expect(scope.isDirtyInvalid testData)
              if testData.expected
                result.is.true
              else
                result.is.false

    describe "Send check", ->
      describe "Success Case", ->
        beforeEach inject [
          "$httpBackend", "$timeout", (backend, timeout) ->
            backend.expectPOST("/u/login").respond 200, ""
            backend.expectGET("/u/login/status").respond 200, ""
            scope.send()
            backend.flush()
            timeout.flush()
        ]
        afterEach inject [
          "$httpBackend", "$timeout", (backend, timeout) ->
            backend.verifyNoOutstandingExpectation()
            backend.verifyNoOutstandingRequest()
            timeout.verifyNoPendingTasks()
        ]
        it "scope.state.go should be called with 'home'", ->
          expect(scope.state.go.calledOnce).is.true
          expect(scope.state.go.calledWithExactly "home").is.true

        it "scope.errors should be undefined", ->
          expect(scope.errors).is.undefined

        it "scope.loginForm.$setPristine shouldn't be called", ->
          expect(scope.loginForm.$setPristine.called).is.false

      describe "Failure Case (/u/login shows 417)", ->
        error = "password": ["This field is required."]
        beforeEach inject [
          "$httpBackend", (backend) ->
            backend.expectPOST("/u/login").respond 417, error
            scope.send()
            backend.flush()
        ]
        afterEach inject [
          "$httpBackend", (backend) ->
            backend.verifyNoOutstandingExpectation()
            backend.verifyNoOutstandingRequest()
        ]
        it "scope.state.go shouldn't be called", ->
          expect(scope.state.go.called).is.false
        it "scope.errors should be proper", ->
          expect(scope.errors.status).is.equal 417
          expect(scope.errors.data).is.eql error
        it "scope.loginForm.$setPristine should be called", ->
          expect(scope.loginForm.$setPristine.called).is.true
      describe "Failure Case (/u/login shows 500)", ->
        beforeEach inject [
          "$httpBackend", (backend) ->
            backend.expectPOST("/u/login").respond 500, ""
            scope.send()
            backend.flush()
        ]
        afterEach inject [
          "$httpBackend", (backend) ->
            backend.verifyNoOutstandingExpectation()
            backend.verifyNoOutstandingRequest()
        ]
        it "scope.state.go shouldn't be called", ->
          expect(scope.state.go.called).is.false
        it "scope.errors should be proper", ->
          expect(scope.errors.status).is.equal 500
          expect(scope.errors.data).is.equal ""
        it "scope.loginForm.$setPristine should be called", ->
          expect(scope.loginForm.$setPristine.called).is.true

      describe "Failure Case (/u/login/status shows 500)", ->
        beforeEach inject [
          "$httpBackend", (backend) ->
            backend.expectPOST("/u/login").respond 200, ""
            backend.expectGET("/u/login/status").respond 500, ""
            scope.send()
            backend.flush()
        ]
        afterEach inject [
          "$httpBackend", (backend) ->
            backend.verifyNoOutstandingExpectation()
            backend.verifyNoOutstandingRequest()
        ]
        it "scope.state.go shouldn't be called", ->
          expect(scope.state.go.called).is.false
        it "scope.errors should be proper", ->
          expect(scope.errors.status).is.equal 500
          expect(scope.errors.data).is.equal ""
        it "scope.loginForm.$setPristine should be called", ->
          expect(scope.loginForm.$setPristine.called).is.true
