from behave import *
from compare import expect
import json

from utils.utils import convert_table_to_dictionary


@when(u'I send a {method} request to {end_point}')
def step_impl(context, method, end_point):
    if context.text:
        project_data = json.loads(context.text)
        context.response = context.request_api.execute_request(method, end_point, data=project_data)
    else:
        context.response = context.request_api.execute_request(method, end_point)


@then(u'I expect status code {status_code}')
def step_impl(context, status_code):
    expect(str(context.response.status_code)).to_equal(status_code)

@when(u'I save the project id as <project_id>')
def step_impl(context):
    context.project_id = (context.response.json())['id']
    print(context.response.json())
    print(context.project_id)


@when(u'I send a {method} request with {end_point} to update the <project_id>')
def step_impl(context, method, end_point):
    end_point_url = end_point + "/" + context.project_id
    context.response = context.request_api.execute_request(method, end_point_url, data=json.loads(context.text))

