import requests
import json
import random
import logging
import pytest


class SlackApi:
    def __init__(self):
        pass

    def generate_request_body(self, **request_json):
        params = {
            "token": "xoxp-882777721875-894245993344-881484420418-b32a318ce981e534b6519d8dd9f2cc69",
            'pretty': '1'
        }
        for key, values in request_json.items():
            params[key] = values
        return params

    def post(self, request_url=None, **data):
        if request_url is None:
            logging.error("Error: Request url is missing")
            raise Exception("Error: Request url is missing")
        params = self.generate_request_body(**data)
        response = requests.post(request_url, params=params)
        return response

    def get(self, request_url=None, **data):
        if request_url is None:
            logging.error("Error: Request url is missing")
            raise Exception("Error: Request url is missing")
        params = self.generate_request_body(**data)
        response = requests.get(request_url, params=params)
        return response

    def put(self, request_url=None, **data):
        if request_url is None:
            logging.error("Error: Request url is missing")
            raise Exception("Error: Request url is missing")
        params = self.generate_request_body(**data)
        response = requests.put(request_url, params=params)
        return response

    def delete(self, request_url=None, **data):
        if request_url is None:
            logging.error("Error: Request url is missing")
            raise Exception("Error: Request url is missing")
        params = self.generate_request_body(**data)
        response = requests.delete(request_url, params=params)
        return response

