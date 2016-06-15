describe "contactResourceTest", ->
  scope = undefined
  res = undefined
  properties = [
    "name", "company", "email", "to", "message",
    "g-recaptcha-response"
  ]

  beforeEach ->
    module "hysoft.contact.resources"

  beforeEach inject [
    "Contact", "$rootScope", (Contact, root) ->
      res = new Contact()
      res.name = "Test Example"
      res.company = "Test Company"
      res.email = "test@example.com"
      res.to = "test"
      res.message = "test"

      scope = root.$new()
      scope.contact = res
      scope.contactForm =
        "$setPristine": sinon.spy()
  ]

  describe "Success case", ->
    beforeEach inject [
      "$httpBackend", (backend) ->
        backend.expectPOST("/contact").respond 200, ""
        res.sendContact "RecaptchaTestToken", scope
    ]

    afterEach inject [
      "$httpBackend", (backend) ->
        backend.verifyNoOutstandingExpectation()
        backend.verifyNoOutstandingRequest()
    ]

    describe "Before request is flushed", ->
      afterEach inject [
        "$httpBackend", (http) ->
          http.flush()
      ]
      it "The model shouldn't be cleared.", ->
          for property in properties
            do (property) ->
              expect(scope.contact).to.have.ownProperty property

      it "contactForm.$setPristine shouldn't be called", ->
        expect(scope.contactForm.$setPristine.called).is.false

    describe "After request is flushed", ->
      beforeEach inject ["$httpBackend", (http) -> http.flush()]

      it "The model shouldn't be cleared yet.", ->
          for property in properties
            do (property) ->
              expect(scope.contact).to.have.ownProperty property

      it "contactForm.$setPristine shouldn't be called", ->
        expect(scope.contactForm.$setPristine.called).is.false

      describe "After the timer is flushed", ->
        beforeEach inject ["$timeout", (timer) -> timer.flush()]
        it "The model should be cleared.", ->
            for property in properties
              do (property) ->
                expect(scope.contact).not.to.have.ownProperty property
        it "contactForm.$setPristine should be called", ->
          expect(scope.contactForm.$setPristine.called).is.true

  describe "Failure 417 case", ->
    beforeEach inject [
      "$httpBackend", (http) ->
        http.expectPOST("/contact").respond 417, {
          "email": ["This field is required."]
        }
        res.sendContact "testToken", scope
        http.flush()
    ]
    afterEach inject [
      "$httpBackend", (http) ->
        http.verifyNoOutstandingExpectation()
        http.verifyNoOutstandingRequest()
    ]
    it "Even if the request is flushed, the model shouldn't be cleared.", ->
      for property in properties
        do (property) ->
          expect(scope.contact).to.have.ownProperty property
    it "The error container should have proper data and status.", ->
      expect(scope.contact.errors.status).to.be.equal 417
      expect(scope.contact.errors.data).to.be.eql(
        "email": ["This field is required."]
      )
    it "Should call $setPristine", ->
      expect(scope.contactForm.$setPristine.called).is.true
