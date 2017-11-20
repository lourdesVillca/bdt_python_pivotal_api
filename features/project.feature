@delete_project
Feature: #Enter feature name here
  # Enter feature description here
  Background: Create a project
    Given I send a POST request to projects
      | name       |
      | Project 01 |
      | Project 02 |

    Then I expect status code 200


  Scenario: list projects
    Given I send a GET request to projects
    Then I expect status code 200