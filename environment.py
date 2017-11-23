import yaml
from utils.api_request import RequestApi
from utils.utils import delete_projects
from utils.utils import delete_workspace

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
        delete_projects(context)


def after_tag(context, tag):
    if tag == 'delete_workspace':
        delete_projects(context)
        delete_workspace(context)
