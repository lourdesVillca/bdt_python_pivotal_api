from behave import given, when, then
from compare import expect
from utils import end_point_util

from utils import json_utils


@given(u'I am logged to pivotal tracker app')
def step_impl(context):
    context.result = context.request_api.execute_request('get', 'projects')


@when(u'I send a {method} method to {end_point} to create a project named {name}')
def step_impl(context, method, end_point, name):
    context.name = name
    data = {"name": name}
    context.result = context.request_api.execute_request(method, end_point,
                                                         json_utils.dictionary_to_json(data))


@then(u'The project should be created')
def step_impl(context):
    expect(context.result.status_code).to_equal(200)


@when(u'I send a {method} method to {end_point} to change the project name to "{name_update}"')
def step_impl(context, method, end_point, name_update):
    new_endpoint = end_point_util.end_point_modifier(end_point, context.result, context.name)
    data = {"name": name_update}
    print(new_endpoint)
    context.result = context.request_api.execute_request(method, new_endpoint,
                                                      json_utils.dictionary_to_json(data))
