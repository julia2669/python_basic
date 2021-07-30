#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/22/2021 17:51 
# @Author : Julia
# @Version：V 0.1
# @File : test_assert.py
# @desc : 断言失败返回信息， 重写断言
import pytest
import allure


def f(self):
    return 3

@allure.story("story: assert")
class TestAllure():
    @allure.testcase("case url","test case: # 1. 用assert 断言")
    def test_function(self):
        assert f(self) == 3


    @allure.testcase("case url","test case: # 2. 指定断言失败返回信息")
    def test_return_message(self):
        a = 1
        assert a % 2 == 0, "值为奇数,应为偶数"



    @allure.testcase("case url","test case: # 3. 异常断言，使用pytest.raises作为上下文管理器")
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0

    @allure.testcase("case url","test case: # 3. 异常断言，使用pytest.raises作为上下文管理器")
    def test_recursion_depth(self):
        with pytest.raises(RuntimeError) as excinfo:
            def f():
                f()

            f()
        assert 'maximum recursion' in str(excinfo.value)


    # 4.上下文管理器表单接受match关键字参数来测试正则表达式匹配中的异常

def myfunc():
    raise ValueError("Exception 123 raised")

@allure.story("story: assert 2")
@allure.testcase("case url","test case: # 4.上下文管理器表单接受match关键字参数来测试正则表达式匹配中的异常")
def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()



class Foo(object):
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val
@allure.story("story: assert 2")
@allure.testcase("case url","test case: # 5. 自定义断言对比/报错信息")
def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
