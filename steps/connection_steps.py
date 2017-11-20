import requests
from compare import expect
from behave import *


@given(u'I connect to pivotal tracker')
def step_impl(context):
    context.result =context.request_api.execute_request('get', 'projects')
    print (context.result.status_code)

@when(u'I login with valid token')
def step_impl(context):
    print(context.token)

@then(u'I should be connected')
def step_impl(context):
    expect(context.result.status_code).to_equal(200)
