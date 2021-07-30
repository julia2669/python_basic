#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 16:39 
# @Author : Julia
# @Version：V 0.1
# @File : test_04_mock.py
# @desc :
import unittest
import mock
import pytest
from .demo_mock import invoke_mock_request
from pytest_mock import mocker

class Count():
    def add(self, a, b):
        return a + b

class MockDemo(unittest.TestCase):
    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8, 8)
        print(result)
        count.add.assert_called_with(8, 8)
        self.assertEqual(result, 16)


def test_get_foo2():
    with mock.patch('demo_mock.mock_request', side_effect=300) as mock_foo:
        assert invoke_mock_request('https://www.python.org/') == mock_foo.return_value


@mock.patch('demo_mock.mock_request', side_effect=300)
def test_get_foo3(mock_request):
    assert invoke_mock_request('https://www.python.org/') == mock_request.return_value

def test_get_foo(mocker):
    mocker.patch('demo_mock.mock_request', return_value=300)
    assert invoke_mock_request('https://www.python.org/') ==300

#上面介绍了对函数或者类进行 mock,
# 有时候测试需要调用依赖于全局设置的功能，或调用无法轻松测试的代码（如网络访问）修改测试环境变量信息等。
# monkey patch fixture 可帮助您安全地设置/删除属性，Monkey patching主要针对模块和环境进行Mock。
# 注意：
#   不建议使用猴子补丁改造Python内置函数，如open，compile等，因为它可能会破坏pytest的内部逻辑。

# 阻止"requests"库在所有测试中执行http请求

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


