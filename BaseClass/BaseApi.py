# -*- coding: utf-8 -*-
#@Pjname ;GhostApiservice
#@Time   :2019/11/26/03:35
#@Author :GhostGuanyin
#@File   :BaseApi.py

import requests

class BaseApi(object):
    url = ""
    params = {}
    method = ""
    headers = {}
    data = ""
    json = {}

    def set_parsms(self, **params):
        self.params = params
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_json(self, json_data):
        self.json = json_data
        return self

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            params=self.params,
            headers=self.headers,
            data=self.data,
            json=self.json
            )
        return self

    def validate(self, key, expected_value):
        actual_value = getattr(self.response, key)
        assert actual_value == expected_value
        return self
