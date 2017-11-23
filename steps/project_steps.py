import json

from behave import *
from compare import expect

use_step_matcher("re")


@then(u'I should expect the following project result')
def step_impl(context):
    project_data = json.loads(context.text)
    for key in project_data:
        expect(context.project_response.json()[key]).to_equal(project_data[key])


