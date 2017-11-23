import json

from behave import when

from utils.utils import map_url


@when(u'I send the {method} request to {end_point}')
def step_impl(context, method, end_point):
    context.project_name = context.project_response.json()['name']
    project_data = json.loads(context.text.replace(context.project_name, str(context.project_response.json()['id'])))
    context.response = context.request_api.execute_request(method, map_url(end_point, context), data=project_data)

