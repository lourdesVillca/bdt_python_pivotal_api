Feature: As a user to pivotal tracker
  I want to test the basic features of workspace

  Background: Create a workspaces
   When I send a POST request to projects
    """
    {
      "name" : "workspace-project01"
    }
    """
#    And I save the project id as <project_id>
#    When I send the POST request to my/workspaces
#    """
#    {
#      "name" : "workspace-auto"
#      "project_ids":[project01]
#    }
#    """
#    And I save the project id as <project_id>
#    Then I expect status code 200
#
   Scenario: Get Workspaces
#    When I send a GET request to my/workspaces
#    Then I expect status code 200