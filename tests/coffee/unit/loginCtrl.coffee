describe "Login Controller Tests", ->
  controller = undefined
  scope = undefined
  beforeEach ->
    module "ngMock"
    module "hysoft.user.controllers"
  beforeEach inject [
    "$rootScope", "$controller", "UserSession", (root, ctrl, User) ->
      scope = root.$new()
      scope.userStatus = new User();
      controller = ctrl "loginController", (
        "$scope": scope
      )
  ]
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
          scope.state = {"go": sinon.spy()}
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
        expect(scope.state.go.calledWith "home").is.true

      it "scope.errors should be undefined", ->
        expect(scope.errors).is.undefined

    describe "Failure Case (/u/login shows 417)", ->
      error = "password": ["This field is required."]
      beforeEach inject [
        "$httpBackend", (backend) ->
          backend.expectPOST("/u/login").respond 417, error
          scope.state = "go": sinon.spy()
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
    describe "Failure Case (/u/login shows 500)", ->
      beforeEach inject [
        "$httpBackend", (backend) ->
          backend.expectPOST("/u/login").respond 500, ""
          scope.state = "go": sinon.spy()
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

    describe "Failure Case (/u/login/status shows 500)", ->
      beforeEach inject [
        "$httpBackend", (backend) ->
          backend.expectPOST("/u/login").respond 200, ""
          backend.expectGET("/u/login/status").respond 500, ""
          scope.state = "go": sinon.spy()
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
