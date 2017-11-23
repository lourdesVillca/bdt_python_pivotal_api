Feature: As a user to pivotal tracker
  I want to test the basic features of workspace

  Background: Create a workspaces
    When I send a POST request to projects
    """
    {
      "name" : "workspace-project01"
    }
    """
    And I save the response as project_response
    When I send the POST request to my/workspaces
    """
    {
      "name" : "workspace-auto",
      "project_ids":[workspace-project01]
    }
    """
    And I save the response as workspace_response
    Then I expect status code 200

  @delete_workspace
  Scenario: Get Workspaces
    When I send a GET request to my/workspaces
    Then I expect status code 200

  @delete_workspace
  Scenario: PUT Workspaces
    Given I send a POST request to projects
    """
    {
      "name" : "workspace-project02"
    }
    """
    And I save the response as project_response
    Then I expect status code 200
    When I send the PUT request to my/workspaces/<workspace_id>
     """
     {
        "project_ids": [workspace-project02]
     }
     """
    Then I expect status code 200

    @delete_workspace
    Scenario: Delete Workspaces
      When I send a DELETE request to my/workspaces/<workspace_id>

      Then I expect status code 204
