#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/22/2021 17:51 
# @Author : Julia
# @Version：V 0.1
# @File : test_assert.py
# @desc : 断言失败返回信息， 重写断言
import pytest
import allure

# 1. 用assert 断言
def f():
    return 3

@allure.feature("test_assert")
@allure.story("exampe_01 用assert 断言")
def test_function():
    assert f() == 3


# 2. 指定断言失败返回信息
@allure.feature("test_assert")
@allure.story("exampe_02 指定断言失败返回信息")
def test_return_message():
    a = 1
    assert a % 2 == 0, "值为奇数,应为偶数"


# 3. 异常断言，使用pytest.raises作为上下文管理器
@allure.feature("test_assert")
@allure.story("exampe_03 异常断言，使用pytest.raises作为上下文管理器")
@allure.testcase("testcase url 01","case 01")
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

@allure.feature("test_assert")
@allure.story("exampe_03 异常断言，使用pytest.raises作为上下文管理器")
@allure.testcase("testcase url 02","case 02")
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    assert 'maximum recursion' in str(excinfo.value)


# 4.上下文管理器表单接受match关键字参数来测试正则表达式匹配中的异常

def myfunc():
    raise ValueError("Exception 123 raised")

@allure.feature("test_assert")
@allure.story("exampe_04 上下文管理器表单接受match关键字参数来测试正则表达式匹配中的异常")
def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()


# 5. 自定义断言对比/报错信息
class Foo(object):
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

@allure.feature("test_assert")
@allure.story("exampe_05 自定义断言对比/报错信息")
def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2

'''
    def test_compare():
        f1 = Foo(1)
        f2 = Foo(2)
>       assert f1 == f2
E       assert Foo实例对比:
E           值: 1 != 2

'''