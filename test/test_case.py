# -*- coding: utf-8 -*-
# @Pjname ;GhostApiservice
# @Time   :2019/11/23/21:19
# @Author :GhostGuanyin
# @File   :test_case.py

import requests


def test_httpbin_get():
   resrt = requests.get(
       "http://www.httpbin.org/get",
       headers={
           "accept": "application/json"
       }
   )
   assert resrt.status_code == 200
   assert resrt.headers["server"] =="nginx"
   assert resrt.json()["url"] =="https://www.httpbin.org/get"


def test_httpbin_get_wich_params():
   resr = requests.get(
       "http://www.httpbin.org/get",
       params="abc=123",
       headers={
           "accept": "application/json"
       }
   )
   assert resr.status_code == 200
   assert resr.headers["server"] =="nginx"
   assert resr.json()["url"] == "https://www.httpbin.org/get?abc=123"

def test_httpbin_post():
   rest = requests.post(
       "http://www.httpbin.org/post",
       headers={
           "accept": "application/json"
           },
       json={"abc":123}
   )
   assert rest.status_code == 200
   assert rest.headers["server"] =="nginx"
   assert rest.json()["url"] == "https://www.httpbin.org/post"
   assert rest.json()["json"]["abc"] == 123