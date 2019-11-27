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


    def extract(self, field):
        value = self.response
        for _key in field.split('.'):
            # print("value====",_key,value)打印调试信息
            if isinstance(value, requests.Response):
                if _key == "json()":  # 可以写成if _key in ["json()","json"]
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]
        # value = getattr(self.response,field)
        return value

    def validate(self, key, expected_value):
        # value = self.response
        # for _key in key.split('.'):
        #     # print("value====",_key,value)打印调试信息
        #     if isinstance(value,requests.Response):
        #         if _key == "json()":  #可以写成if _key in ["json()","json"]
        #             value = self.response.json()
        #         else:
        #             value = getattr(value, _key)
        #     elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
        #         value = value[_key]
        # print("value====", _key, value,expected_value)打印调试信息

        actual_value = self.extract(key)
        assert actual_value == expected_value
        return self
