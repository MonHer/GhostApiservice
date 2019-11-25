# -*- coding: utf-8 -*-
#@Pjname ;GhostApiservice
#@Time   :2019/11/21/02:02
#@Author :GhostGuanyin
#@File   :test_Apiservice.py

def test_version():
    from Apiservice import __version__
    assert isinstance(__version__,str)


