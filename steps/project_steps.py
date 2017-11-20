from behave import *
from compare import expect
import json

from utils.utils import convert_table_to_dictionary


@given(u'I send a {method} request to {end_point}')
def step_impl(context, method, end_point):
    if context.table:
        data_table = convert_table_to_dictionary(context.table)
        for row_data in data_table:
            context.response = context.request_api.execute_request(method, end_point, data=row_data)
    else:
        context.response = context.request_api.execute_request(method, end_point)


@then(u'I expect status code {status_code}')
def step_impl(context, status_code):
    expect(str(context.response.status_code)).to_equal(status_code)


