Feature:
  As a user to pivotal tracker
  I want to test the basic features of projects

  Background: Create a project
    When I send a POST request to projects
    """
    {
      "name" : "project 01"
    }
    """
      And I save the project id as <project_id>
    Then I expect status code 200

  @smoke, @delete_project
  Scenario: Get Projects
    When I send a GET request to projects
    Then I expect status code 200

  @delete_project
  Scenario: Put Projects
    When I send a PUT request to projects/<project_id>
    """
    {
    "name" : "Update-Project"
    }
    """

  @delete_project
  Scenario: Delete Projects
    When I send a DELETE request to projects/<project_id>
    Then I expect status code 204


