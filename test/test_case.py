# -*- coding: utf-8 -*-
# @Pjname ;GhostApiservice
# @Time   :2019/11/23/21:19
# @Author :GhostGuanyin
# @File   :test_case.py

import pytest
from Httpbin.httpbin import *


def test_httpbin_get():
   ApihttpbinGet().run()\
       .validate("json().args",{})\
       .validate("status_code",200)\
       .validate("headers.server","nginx")\
       .validate("json().url","https://www.httpbin.org/get")\
       .validate("json().headers.Accept","application/json")\


def test_httpbin_get_wich_params():
    ApihttpbinGet()\
        .set_params(abc=123,asd=456)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server","nginx")\
        .validate("json().headers.Accept","application/json")\
        .validate("json().args",{"abc": "123","asd": "456"})\
        .validate("json().url","https://www.httpbin.org/get?abc=123&asd=456")


def test_httpbin_post():
   ApihttpbinPost()\
       .set_json({"abc":456})\
       .run()\
       .validate("json().args",{})\
       .validate("status_code",200)\
       .validate("headers.server","nginx")\
       .validate("json().headers.Accept","application/json")\
       .validate("json().url","https://www.httpbin.org/post") \
       .validate("json().headers.Accept-Encoding", "gzip, deflate")


def test_httpbin_parameters_share(): #实现多个接口参数共享同一个参数
    user_id = "abk124"
    ApihttpbinGet() \
        .set_params(user_id=user_id) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "nginx") \
        .validate("json().headers.Accept","application/json")\
        .validate("json().args", {"user_id": "abk124"}) \
        .validate("json().url", "https://www.httpbin.org/get?user_id={}".format(user_id))

    ApihttpbinPost()\
        .set_data({"user_id":user_id})\
        .run()\
        .validate("json().args", {})\
        .validate("status_code", 200)\
        .validate("headers.server", "nginx")\
        .validate("json().headers.Accept","application/json")\
        .validate("json().url", "https://www.httpbin.org/post")\
        .validate("json().headers.Accept-Encoding", "gzip, deflate")


# boby参数提取实验
def test_httpbin_extract(init_session):
    status_code = ApihttpbinGet().run().extract("status_code")
    assert status_code == 200

    server = ApihttpbinGet().run().extract("headers.server")
    assert server == "nginx"

    Length_value = ApihttpbinGet().run().extract("json().headers.Content-Length")
    assert Length_value == "2"


# 提取cookiesdome
def test_Getcookies():
    Getcookies_run = ApihttpbinGetcookies()\
        .set_cookie("cookies","lll")\
        .run()
    Getcookies = Getcookies_run.extract("json().cookies.cookies")
    assert Getcookies == "lll"

    # 关联参数
    ApihttpbinPost() \
        .set_json({"Getcookies": Getcookies}) \
        .run() \
        .validate("json().args", {}) \
        .validate("status_code", 200) \
        .validate("headers.server", "nginx") \
        .validate("json().headers.Accept", "application/json") \
        .validate("json().url", "https://www.httpbin.org/post") \
        .validate("json().headers.Accept-Encoding", "gzip, deflate")


# 登录验收
def test_httpbin_login_status(init_session):
	#print("init_session====",init_session)
	#step1:login and get cookie
	ApihttpbinSetCookies().set_params(freeform="123").run(init_session)

	#step2:
	resp = ApihttpbinPost() \
		.set_json({"abc": 123}) \
		.run().get_response()
	request_headers = resp.request.headers
	# assert 'freeform=123' in request_headers["Cookie"]
	print("request_headers====",request_headers)
