# -*- coding: utf-8 -*-
# @Pjname ;GhostApiservice
# @Time   :2019/11/23/21:19
# @Author :GhostGuanyin
# @File   :test_case.py


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
        .set_parsms(abc=123,asd=456)\
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
        .set_parsms(user_id=user_id) \
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


def test_httpbin_extract():
    status_code = ApihttpbinGet().run().extract("status_code")
    assert status_code == 200

    server = ApihttpbinGet().run().extract("headers.server")
    assert server == "nginx"


    Length_value = ApihttpbinGet().run().extract("json().headers.Content-Length")
    assert Length_value == "2"