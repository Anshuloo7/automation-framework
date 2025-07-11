Feature: Sample Behave Test

  Scenario: Test that the automation framework is connected
    Given I hit the demo API
    Then I should get a successful response
