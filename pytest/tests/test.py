#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 13:00 
# @Author : Julia
# @Version：V 0.1
# @File : test.py
# @desc :
import json
import pytest


def test_json():
    j1s = {
        'name':'julia'
    }
    j2s = {
        'name':'julia'
    }
    j1 = json.dumps(j1s)
    j2=json.dumps(j2s)
    assert j1 == j2s

if __name__ == '__main__':
    pytest.main(['-s','-v','test.py'])
