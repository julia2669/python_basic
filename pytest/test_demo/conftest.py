#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/22/2021 18:53 
# @Author : Julia
# @Version：V 0.1
# @File : conftest.py
# @desc :
import sys
# sys.path.append(r'C:\Users\julizhou\PycharmProjects\python_basic')
# print(sys.path)
from .test_01_assert import Foo
import pytest
import random

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return ['Foo实例对比:',
                '  值: %s != %s' % (left.val, right.val)]


@pytest.fixture
def fixture_in_config():
    return "fixture in configtest"

@pytest.fixture
def load_text():
    s=''
    with open('test.txt','r') as f:
        s=f.read()
    return s


#pytest_generate_tests 在测试用例参数化收集前调用此钩子函数，根据测试配置或定义测试函数的类或模块中指定的参数值生成测试用例，

def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )

def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput",metafunc.config.getoption("stringinput"))



# 通过fixtureRequest 。config 。cache 拿到cache的值
@pytest.fixture
def mydata(request):
    val = request.config.cache.get("example/value",None)
    if val is None:
        # do something
        val = 42
        request.config.cache.set("example/value",val)
    return val