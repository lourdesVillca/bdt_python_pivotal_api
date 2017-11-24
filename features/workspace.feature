# Created by Alvaro at 22/11/2017
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

  @smoke
  @delete_workspace
  Scenario: Get Workspaces
    When I send a GET request to my/workspaces
    Then I expect status code 200

  @smoke
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

  @smoke
  @delete_workspace
  Scenario: Delete Workspaces
    When I send a DELETE request to my/workspaces/<workspace_id>
    Then I expect status code 204

  @crud
  @delete_workspace
  Scenario: The workspace created with a specific name and contains a specific project
    When I send a GET request to my/workspaces
    Then the workspace created should contain the following data:
    """
    {
      "name" : "workspace-auto"
    }
    """
    And the workspace should contain the project created
