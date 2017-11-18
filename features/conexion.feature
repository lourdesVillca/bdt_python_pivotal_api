Feature: Connection to pivotal
  Scenario: Validate Connection
    Given I connect to pivotal tracker
    When I login with valid token
    Then I should be connected