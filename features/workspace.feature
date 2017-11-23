Feature: As a user to pivotal tracker
  I want to test the basic features of workspace

  Background: Create a workspaces
    When I send a POST request to projects
    """
    {
      "name" : "workspace-project01"
    }
    """
    And I save the project id as <project_id>
    When I send the POST request to my/workspaces
    """
    {
      "name" : "workspace-auto",
      "project_ids":[workspace-project01]
    }
    """
     And I save the workspaces id as <workspaces_id>
    Then I expect status code 200


#  @delete_workspace
#  Scenario: Get Workspaces
#    When I send a GET request to my/workspaces
#    Then I expect status code 200
#
#  @delete_workspace
#  Scenario: PUT Workspaces
#    When I send PUT request to my/workspaces/<workspaces_id>
#     """
#     {
#     "project_ids":[workspace-project01]
#     }
#     """
#    Then I expect status code 200
#
  @delete_workspace
  Scenario: Delete Workspaces
    When I send a DELETE request to my/workspaces/<workspaces_id>
    Then I expect status code 204
