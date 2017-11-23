import yaml
from utils.api_request import RequestApi

global generic_data
global request_api

generic_data = yaml.load(open('../config/config.yml'))


def before_all(context):
    context.url = generic_data['app']['url']
    context.token = generic_data['app']['account']['token']
    context.username = generic_data['app']['account']['username']
    context.password = generic_data['app']['account']['password']
    context.request_api = RequestApi(context.token, context.url, context.username, context.password)



def before_tag(context, tag):
    if tag == 'delete_project':
        project_list = context.request_api.execute_request('get', 'projects')
        if project_list.json():
            for project in project_list.json():
                delete_url = 'projects/' + str(project['id'])
                context.request_api.execute_request('delete', delete_url)

def after_tag(context, tag):
    pass
    # if tag == 'delete_workspace':
    #     project_list = context.request_api.execute_request('get', 'projects')
    #     if project_list.json():
    #         for project in project_list.json():
    #             print("delete_url", project['id'])
    #             delete_url = 'projects/' + str(project['id'])
    #
    #             context.request_api.execute_request('delete', delete_url)