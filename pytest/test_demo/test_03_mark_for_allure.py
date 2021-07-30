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
import allure

@allure.feature("feature: test_03_mark, feature mark at class level")
class TestMark():
    @allure.story("story: story in class")
    @pytest.mark.slow
    def test_demo01(self):
        print("函数级别的test_demo01")

    @allure.story("story: story in class")
    @pytest.mark.smoke
    def test_demo02(self):
        print("函数级别的test_demo02")


    @allure.story("story: story marked at class level in a class")
    @pytest.mark.demo
    class TestDemo:
        @allure.testcase("test case url","test cases in a class")
        def test_demo01(self):
            print("test_demo01")

        @allure.testcase("test case url","test cases in a class")
        @pytest.mark.regression
        def test_demo02(self):
            print("test_demo02")

    @allure.story("story: story in class")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_regression(self):
        print("test_demo02")

    @allure.story("story: story in class")
    @pytest.mark.xfail(condition=(5>1),reason = "comments")
    def test_mark_xfail(self):
        assert 0 == 1

    @allure.story("story: story in class")
    @pytest.mark.xfail(raises=AssertionError)
    def test_01(self):
        assert 1 == 2

    @allure.story("story: story in class")
    @pytest.mark.xfail(raises=ValueError)
    def test_02(self):
        if isinstance('1234', int) is not True:
            raise TypeError("传入参数非整数")