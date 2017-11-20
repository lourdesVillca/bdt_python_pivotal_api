from behave import *


@given(u'I connect to pivotal tracker')
def step_impl(context):
    result =context.request_api.execute_request('get', 'projects', data=None)
    print (result.status_code)

@when(u'I login with valid token')
def step_impl(context):
    print(context.token)

@then(u'I should be connected')
def step_impl(context):
    print("CONNECTED")
