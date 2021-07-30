#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/22/2021 15:18 
# @Author : Julia
# @Version：V 0.1
# @File : testCases_inClass.py
# @desc :
import re
import unittest


class NameCheck():
    def __init__(self):
        self.pattern = "^[a-zA-Z](?=\w*\d+\w*)[a-zA-Z0-9]{1,19}$"  # 用^和$ 限定从开头到结尾完全匹配或者用fullmatch来限制

    def name_check(self, name):
        m = re.match(self.pattern, name)
        if m is not None:
            return "Accept"
        else:
            return "Wrong"


class TestNameCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nameCheck = NameCheck()
        cls.a = 0
        print(f"setup in class, a ={cls.a}")

    @classmethod
    def tearDownClass(cls):
        cls.a = 0
        print(f"teardown in class, a ={cls.a}")

    def setUp(self):
        self.a = 1
        self.b = 1
        print(f"setup in method, a ={self.a}")

    def tearDown(self):
        self.a = 2
        print(f'teardown in method, a ={self.a}')

    def test_nameCheck_01(self):
        self.name = 'a3'
        print(self.a)
        assert self.nameCheck.name_check(self.name) == 'Accept'

    def test_nameCheck_02(self):
        self.name = 'a3'
        self.assertEqual(self.nameCheck.name_check(self.name), "Accept")

    def test_nameCheck_03(self):
        self.name = '3'
        self.assertEqual(self.nameCheck.name_check(self.name), "Wrong")
