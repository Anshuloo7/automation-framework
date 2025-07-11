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

  @db @regression
  Scenario: Verify user exists in DB
    Then I should see user 'Alice' in the database

  @faker @regression
  Scenario: Generate a random user
    Given I generate a random user

  @e2e @regression
  Scenario: Full flow — generate, insert, and verify user
    Given I create and insert a random user
    Then I should find that user in the database

