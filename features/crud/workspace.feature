@crud
@workspace
Feature: As a user to pivotal tracker
  I want to test the CRUD validations for workspace Endpoints

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
  Scenario: The workspace created with a specific name and contains a specific project
    When I send a GET request to my/workspaces
    Then the workspace created should contain the following data
    """
    {
      "name" : "workspace-auto"
    }
    """
    And the workspace should contain the project created