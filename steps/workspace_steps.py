import json

from behave import when


@when(u'I send the {method} request to {end_point}')
def step_impl(context, method, end_point):
    context.project_name = context.response.json()['name']
    project_data = json.loads(context.text.replace(context.project_name, str(context.response.json()['id'])))
    context.response = context.request_api.execute_request(method, end_point, data=project_data)


@when(u'I save the workspaces id as <workspaces_id>')
def step_impl(context):
    context.workspace_response = context.response


@when(u'I send {method} request to {end_point}')
def step_impl(context, method, end_point):
    end_point = end_point.replace('<workspaces_id>', str(context.workspace_response.json()['id']))
    project_data = json.loads(context.text.replace(context.project_name, str(context.project_response.json()['id'])))
    context.response = context.request_api.execute_request(method, end_point, data=project_data)
