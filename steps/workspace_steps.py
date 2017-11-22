from behave import when


@when(u'I send the POST request to (.*)')
def step_impl(context, method, end_point):
    print ('ESTOY ENTRANDO AL POST')
    pass
    # if context.text:
    #     project_data = json.loads(context.text)
    #     context.response = context.request_api.execute_request(method, end_point, data=project_data)
    #     print(context.response.status_code)
    # else:
    #     context.response = context.request_api.execute_request(method, end_point)
