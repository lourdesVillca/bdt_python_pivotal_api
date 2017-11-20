import yaml
from utils.api_request import RequestApi
global generic_data
global request_api

generic_data =yaml.load(open('config/config.yml'))

def before_all(context):
    context.url = generic_data['app']['url']
    context.token = generic_data['app']['account']['token']
    context.username = generic_data['app']['account']['username']
    context.password = generic_data['app']['account']['password']
    context.request_api = RequestApi(context.token,context.url,context.username,context.password)
    # d = request_api.get_request('get','projects')
