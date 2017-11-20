Feature: As a user of the pivotal tracker app
  I want to test all basics features of projects
Background: Preconditions
  Given I am logged to pivotal tracker app

#  Scenario Outline: Create a project
#    When I send a Post method to projects to create a project named <name>
#    Then The project should be created
#    Examples:
#      | name         |
#      | Auto-Project |

  Scenario Outline: Update a project
    When I send a Post method to projects to create a project named <name>
      And I send a Put method to projects/<name> to change the project name to "New-Auto-Project"
    Then The project should be created
    Examples:
      | name         |
      | Auto-Project |

