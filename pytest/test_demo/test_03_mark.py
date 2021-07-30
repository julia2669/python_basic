# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 15:54
# @Author : Julia
# @Version：V 0.1
# @File : test_03_mark.py
# @desc :一些常用的内置标记：
#     skip - 始终跳过该测试用例
#     skipif - 遇到特定情况跳过该测试用例
#     xfail - 遇到特定情况,产生一个“期望失败”输出, 期望测试用例是失败的，但是不会影响测试用例的的执行
#     parametrize - 在同一个测试用例上运行多次调用(译者注: 参数化数据驱动)
#       注意：
#       标记只对测试用例有效,对fixtures方法无效
#       pytest -m demo
#       pytest -m "demo and not regression" -s

import pytest
import allure

@pytest.mark.slow
def test_demo01():
    print("函数级别的test_demo01")


@pytest.mark.smoke
def test_demo02():
    print("函数级别的test_demo02")


@pytest.mark.demo
class TestDemo:
    def test_demo01(self):
        print("test_demo01")

    @pytest.mark.regression
    def test_demo02(self):
        print("test_demo02")

@pytest.mark.smoke
@pytest.mark.regression
def test_regression():
    print("test_demo02")



@pytest.mark.xfail(condition=(5>1),reason = "comments")
def test_mark_xfail():
    assert 0 == 1


@pytest.mark.xfail(raises=AssertionError)
def test_01():
    assert 1 == 2

# 具体的说明测试失败的原因。可以在raises参数中指定单个异常或异常组，如果测试失败且没有提到指定的异常，那么测试将被报告为常规失败raises
@pytest.mark.xfail(raises=ValueError)
def test_02():
    if isinstance('1234', int) is not True:
        raise TypeError("传入参数非整数")