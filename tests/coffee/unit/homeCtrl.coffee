describe "Home controller tests", ->
  scope = undefined
  valStub = undefined
  findStub = undefined

  beforeEach ->
    module "hysoft.home.controller"

  beforeEach inject [
    "$controller", "$rootScope", (ctrl, root) ->
      valStub = sinon.stub().returns("test")
      findStub = sinon.stub().returns(("val": valStub))

      class ElementMock
        constructor: ->
        find: findStub

      scope = root.$new()
      scope.contactForm = (
        "$setPristine": sinon.spy()
      )
      ctrl "homeController", (
        "$scope": scope,
        "$element": new ElementMock()
      )
  ]

  prepareData = ->
    scope.contact.name = "Test Example"
    scope.contact.company = "Test Company"
    scope.contact.email = "test@example.com"
    scope.contact.to = "test"
    scope.contact.message = "test"

  describe "Contact functionality tests", ->
    describe "Success Case", ->
      beforeEach inject [
        "$httpBackend", (http) ->
          prepareData()
          http.expectPOST("/contact/#{scope.contact.to}").respond 200, ""
          scope.sendContact()
      ]
      afterEach inject [
        "$httpBackend", (http) ->
          http.verifyNoOutstandingExpectation()
          http.verifyNoOutstandingRequest()
      ]
      it "Before the request is flushed, the model shouldn't be cleared.",
        inject [
          "$httpBackend", (http) ->
            properties = [
                "name", "company", "email", "to", "message",
                "g-recaptcha-response"
            ]
            for property in properties
              do (property) ->
                expect(scope.contact).to.have.ownProperty property
            http.flush()
        ]

      it "After the request is flushed, the model should be cleared.",
        inject [
          "$httpBackend", (http) ->
            http.flush()
            properties = [
              "name", "company", "email", "to", "message",
              "g-recaptcha-response"
            ]
            for property in properties
              do (property) ->
                expect(scope.contact).not.to.have.ownProperty property
        ]

    describe "Failure 417 case", ->
      beforeEach inject [
        "$httpBackend", (http) ->
          prepareData()
          http.expectPOST("/contact/#{scope.contact.to}").respond 417, {
            "email": ["This field is required."]
          }
          scope.sendContact()
          http.flush()
      ]
      afterEach inject [
        "$httpBackend", (http) ->
          http.verifyNoOutstandingExpectation()
          http.verifyNoOutstandingRequest()
      ]
      it "Even if the request is flushed, the model shouldn't be cleared.", ->
        properties = [
          "name", "company", "email", "to", "message",
          "g-recaptcha-response"
        ]
        for property in properties
          do (property) ->
            expect(scope.contact).to.have.ownProperty property
      it "The error container should have proper data and status.", ->
        expect(scope.contactErrors.status).to.be.equal 417
        expect(scope.contactErrors.data).to.be.eql(
          "email": ["This field is required."]
        )
      it "Should call $setPristine", ->
        expect(scope.contactForm.$setPristine.called).is.true
