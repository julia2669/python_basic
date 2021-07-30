#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/10/2021 10:31 
# @Author : Julia
# @Version：V 0.1
# @File : switch.py
# @desc :

'''
Python 中没有 switch语句。
一般用if-else 语句可以替代switch语句，今天用字典的映射来代替switch语句，
'''


def case1():                            # 第一种情况执行的函数
    print('This is the case1')


def case2():                            # 第二种情况执行的函数
    print('This is the case2')


def case3():                            # 第三种情况执行的函数
    print('This is the case3')


def default():                          # 默认情况下执行的函数
    print('No such case')


switch = {'case1': case1,                # 注意此处不要加括号
          'case2': case2,
          'case3': case3,
          }

choice = 'case1'                         # 获取选择
switch.get(choice, default)()            # 执行对应的函数，如果没有就执行默认的函数