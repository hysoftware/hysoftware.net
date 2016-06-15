describe "Contact controller tests", ->
  scope = undefined
  valval = "test"
  valStub = undefined
  findStub = undefined

  beforeEach ->
    module "hysoft.contact.controllers"

  beforeEach inject [
    "$controller", "$rootScope", (ctrl, root) ->
      valStub = sinon.stub().returns(valval)
      findStub = sinon.stub().returns(("val": valStub))

      class ElementMock
        constructor: ->
        find: findStub

      scope = root.$new()
      scope.contactForm = (
        "$setPristine": ->
      )
      ctrl "contactController", (
        "$scope": scope,
        "$element": new ElementMock()
      )
      scope.contact.sendContact = sinon.spy()
  ]

  describe "sendContact", ->
    beforeEach ->
      scope.sendContact()
    it "should call $element.find to find recaptcha token", ->
      expect(findStub.callCount).is.equal 1
      expect(findStub.calledWithExactly(
        "form#contactForm [name='g-recaptcha-response']"
      )).is.true
      expect(valStub.callCount).is.equal 1
    it "Should be called scope.contact.sendContact properly", ->
      expect(scope.contact.sendContact.calledWithExactly valval, scope).is.true
