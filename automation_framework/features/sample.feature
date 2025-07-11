Feature: Sample Behave Test

  @smoke
  Scenario: Test that the automation framework is connected
    Given I hit the demo API
    Then I should get a successful response

  @sanity @regression
  Scenario: Test GET with query params
    Given I hit the demo API with query "foo=bar"
    Then I should get a successful response

  @negative @regression
  Scenario: Test invalid endpoint
    Given I hit an invalid API endpoint
    Then I should get a 404 response
