Feature:
  As a user to pivotal tracker
  I want to test the CRUD validations for Story Endpoints

  Background:
    Given I send a POST request to projects
    """
    {
      "name" : "project crud-01"
    }
    """
    And I save the response as project_response
    Then I expect status code 200

  @delete_project
  Scenario: CRUD - Verify data info for created project
    When I send a POST request to /projects/<project_id>/stories
      """
        {
          "name" : "Story crud-01",
          "current_state": "started",
          "story_type": "feature",
          "estimate": 2
        }
      """
    And I save the response as story_response
    Then I expect status code 200
      And I expect the story response should contain the following info
      """
        {
          "name": "Story crud-01",
          "current_state": "started",
          "story_type": "feature",
          "estimate": 2
        }
      """