#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 15:40 
# @Author : Julia
# @Version：V 0.1
# @File : test_setenv.py
# @desc :
import os
import pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit(object):
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile","w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []