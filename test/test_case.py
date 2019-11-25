# -*- coding: utf-8 -*-
# @Pjname ;GhostApiservice
# @Time   :2019/11/23/21:19
# @Author :GhostGuanyin
# @File   :test_case.py


from BaseClass import BaseApi


class ApihttpbinGet(BaseApi):
    url = "http://www.httpbin.org/get"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}


class ApihttpbinPost(BaseApi):
    url = "http://www.httpbin.org/post"
    method = "POST"
    headers = {"accept": "application/json"}
    data = "abc = 123"
    json = {"abc":123}

def test_httpbin_get():
   ApihttpbinGet().run()\
       .validate("status_code",200)\
       # .validate("headers.server","nginx")\
       # .validate("json.url","https://www.httpbin.org/get")


def test_httpbin_get_wich_params():
    ApihttpbinGet()\
        .set_parsms(abc=123,asd=456)\
        .run()\
        .validate("status_code",200)

def test_httpbin_post():
   ApihttpbinPost()\
       .set_json({"abc":456})\
       .run()\
       .validate("status_code",200)