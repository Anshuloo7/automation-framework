Feature: Sample Behave Test

  @smoke
  Scenario: Test that the automation framework is connected
    Given I hit the demo API
    Then I should get a successful response

  @sanity @regression
  Scenario Outline: Test GET with query params
    Given I hit the demo API with query "<query>"
    Then I should get a successful response

    Examples:
      | query      |
      | foo=bar    |
      | key=value  |
      | id=123     |

  @negative @regression
  Scenario: Test invalid endpoint
    Given I hit an invalid API endpoint
    Then I should get a 404 response

  @regression @datatable
  Scenario: Hit demo API with multiple query parameters
    Given I hit the demo API with
      | key   | value  |
      | foo   | bar    |
      | alpha | beta   |
    Then I should get a successful response


