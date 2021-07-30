#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/22/2021 16:07 
# @Author : Julia
# @Version：V 0.1
# @File : test_xfail.py
# @desc : 执行命令：pytest --runxfail，也就是--runxfail参数可以将全部@pytest.mark.xfail()标识忽略掉。
import pytest

@pytest.mark.xfail(True, reason="该功能尚未完成")
def test_case_1():
    print("预期失败,结果失败")
    pytest.xfail()
    assert False

@pytest.mark.xfail(True, reason="该功能尚未计划")
def test_case_2():
    print("预期失败,结果成功")
    assert True

@pytest.mark.xfail(False, reason="")
def test_case_3():
    print("预期成功,结果失败")
    assert False

@pytest.mark.xfail(False, reason="")
def test_case_4():
    print("预期成功,结果成功")
    assert True


