# Created by LuLy at 21/11/2017
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
    And I save the project id as <project_id>
    Then I expect status code 200


    When I send a POST request to /projects/<project_id>/stories
    """
    {
      "name" : "Story 01",
      "current_state" : "unscheduled",
      "story_type" : "feature"
    }
    """
    Then I expect status code 200

  @delete_project
  Scenario: Get Stories
    When I send a GET request to /projects/stories
    Then I expect status code 200