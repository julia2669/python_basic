#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 16:49 
# @Author : Julia
# @Version：V 0.1
# @File : demo_mock.py
# @desc :

import requests
import os
import sys
sys.path.append(os.pardir)
print(os.pardir)

def mock_request(url):
    return requests.get(url).status_code

def invoke_mock_request(url):
    return mock_request()