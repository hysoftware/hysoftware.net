describe "Form Validation Check", ->
  beforeEach ->
    module "hysoft.common.form.validation"

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
          it "Should return #{testData.expected}", inject [
              "isDirtyInvalid", (isDirtyInvalid) ->
                result = expect(isDirtyInvalid testData)
                if testData.expected
                  result.is.true
                else
                  result.is.false
            ]
