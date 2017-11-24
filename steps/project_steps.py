import json

from behave import *
from compare import expect

from utils.utils import convert_table_to_dictionary, map_url

use_step_matcher("re")


@then(u'I expect the project response should contain the following info')
def step_impl(context):
    project_data = json.loads(context.text)
    for key in project_data:
        expect(context.project_response.json()[key]).to_equal(project_data[key])


@given(u'I send a (POST) request to (.*) with table')
def step_impl(context, method, end_point):
    context.data_table = convert_table_to_dictionary(context.table)
    for row_data in context.data_table:
        context.response = context.request_api.execute_request(method, map_url(end_point, context), data=row_data)


@then(u'I expect the response should contains all created projects')
def step_impl(context):
    project_result_list = context.response.json()
    for index, row_data in enumerate(context.data_table):
        for key in row_data:
            expect(project_result_list[index][key]).to_equal(row_data[key])

@then(u'I expect the response result list should be (.*)')
def step_impl(context, records_number):
    expect(len(context.response.json())).to_equal(int(records_number))