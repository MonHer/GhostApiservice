# -*- coding: utf-8 -*-
#@Pjname ;GhostApiservice
#@Time   :2019/11/28/03:05
#@Author :GhostGuanyin
#@File   :conftest.py

import pytest
import requests

@pytest.fixture
def init_session():
	return requests.sessions.session()