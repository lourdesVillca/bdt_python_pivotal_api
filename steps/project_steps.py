import re
import json
from behave import *
from compare import expect

use_step_matcher("re")


@when(u'I send a (GET|POST) request to (.*)')
def step_impl(context, method, end_point):
    if context.text:
        project_data = json.loads(context.text)
        context.response = context.request_api.execute_request(method, end_point, data=project_data)
        print(context.response.status_code)
    else:
        context.response = context.request_api.execute_request(method, end_point)


@then(u'I expect status code (.*)')
def step_impl(context, status_code):
    expect(str(context.response.status_code)).to_equal(status_code)


@when(u'I save the project id as <project_id>')
def step_impl(context):
    context.project_id = (context.response.json())['id']
    print(context.response.status_code)
    print( context.project_id)


@when(u'I send a (PUT|DELETE) request to (.*)')
def step_impl(context, method, end_point):
    end_point_url = re.sub("<.*>", str(context.project_id), end_point)
    context.response = context.request_api.execute_request(method, end_point_url, data=json.loads(context.text))
