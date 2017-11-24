@story
@smoke
Feature:
  As a user to pivotal tracker
  I want to test basic features of projects

  Background:
    When I send a POST request to /projects
    """
    {
      "name" : "project 01"
    }
    """
    And I save the response as project_response
    Then I expect status code 200


    When I send a POST request to /projects/<project_id>/stories
    """
    {
      "name" : "Story 01",
      "current_state" : "unscheduled",
      "story_type" : "feature"
    }
    """
    And I save the response as story_response
    Then I expect status code 200

  @smoke_get_story
  @delete_project
  Scenario: Get Stories
    When I send a GET request to /projects/<project_id>/stories
    Then I expect status code 200

  @smoke_put_story
  @delete_project
  Scenario: Put Story
    When I send a PUT request to projects/<project_id>/stories/<story_id>
    """
    {
      "name" : "Story 01 - updated"
    }
    """
    Then I expect status code 200

  @smoke_delete_story
  @delete_project
  Scenario: Delete Story
    When I send a DELETE request to projects/<project_id>/stories/<story_id>
    Then I expect status code 204