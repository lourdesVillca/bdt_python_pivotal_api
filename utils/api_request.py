import requests
import json
from requests.auth import HTTPBasicAuth


class RequestApi:
    def __init__(self, token, url, username, password):
        self.token = token
        self.base_endpoint = url
        self.authorizarion = (username, password)
        self.headers = {'X-TrackerToken': token}

    def execute_request(self, method, end_point, data=None):
        return requests.request(method, self.base_endpoint + end_point, headers=self.headers, data=data)
