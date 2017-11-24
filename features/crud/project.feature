Feature:
  As a user to pivotal tracker
  I want to test the CRUD validations for Project Endpoints

  @delete_project
  Scenario: CRUD - Verify data info for created project
    When I send a POST request to projects
    """
    {
      "name" : "project crud-01",
      "project_type": "demo",
      "public": false,
      "iteration_length": 1,
      "week_start_day": "Monday",
      "point_scale": "0,1,2,3",
      "start_date":  "2017-11-27",
      "initial_velocity":10
    }
    """
    And I save the response as project_response
    Then I expect status code 200
      And I expect the project response should contain the created project data

  @delete_project
  Scenario: CRUD - Verify Project List for created project
    Given I send a POST request to projects with table
      | name       | project_type | public |
      | Project 01 | demo         | false  |
      | Project 02 | public       | true   |

    When I send a GET request to projects
    Then I expect the response should contains all created projects
      And I expect the response result list should be 2