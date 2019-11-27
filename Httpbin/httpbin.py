# -*- coding: utf-8 -*-
#@Pjname ;GhostApiservice
#@Time   :2019/11/27/22:23
#@Author :GhostGuanyin
#@File   :httpbin.py

from BaseClass.BaseApi import BaseApi

class ApihttpbinGet(BaseApi):
    url = "http://www.httpbin.org/get"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}


class ApihttpbinPost(BaseApi):
    url = "http://www.httpbin.org/post"
    method = "POST"
    headers = {"accept": "application/json"}
    data = ""
    json = {"abc":123}


class ApihttpbinGetcookies(BaseApi):
    url = "http://www.httpbin.org/cookies"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}