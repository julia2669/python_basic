#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/27/2021 12:02 
# @Author : Julia
# @Version：V 0.1
# @File : test_todoapp.py
# @desc :

import pytest
from utils.operate_data import OperateData
import requests
import json

od = OperateData()
testdata = od.readYaml(filedir='data',file='todo.yaml')

@pytest.mark.parametrize('case',testdata)
def test_todo_app(case):
    resp = requests.request(method=case['method'],
                            url=case['url'],
                            json=case.get('body',None),
                            headers = {
                                'Content-Type': 'application/json'
                            }
                            )

    assert resp.status_code==case['expect']['status_code']
    assert case['expect'].get('body') == eval(json.dumps(resp.json()))
#
if __name__ == '__main__':
    pytest.main(['-svv','test_todoapp.py'])