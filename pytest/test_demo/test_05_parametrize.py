#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 17:25 
# @Author : Julia
# @Version：V 0.1
# @File : test_05_parametrize.py
# @desc :   pytest 实现参数化有三种方式
#     pytest.fixture() 使用 fixture 传 params 参数实现参数化
#     @ pytest.mark.parametrize 允许在测试函数或类中定义多组参数，在用例中实现参数化
#     pytest_generate_tests 允许定义自定义参数化方案或扩展。

import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5",8),
     ("2+4",6),
     pytest.param("6*9",42,marks=pytest.mark.xfail)],
    )
def test_eval(test_input,expected):
    assert eval(test_input) == expected


#     pytest_generate_tests 允许定义自定义参数化方案或扩展。
#     pytest -q --stringinput="hello" --stringinput="world" test_05_parametrize.py
def test_valid_string(stringinput):
    assert stringinput.isalpha()