import json

from behave import *
from compare import expect

use_step_matcher("re")


@then(u'I expect the story response should contain the created story data')
def step_impl(context):
    story_data = context.object_data
    for key in story_data:
        expect(context.story_response.json()[key]).to_equal(story_data[key])
