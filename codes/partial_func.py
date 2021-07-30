#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 16:12 
# @Author : Julia
# @Version：V 0.1
# @File : partial_func.py
# @desc :   在task执行完毕的时候可以获取执行的结果，回调的最后一个参数是future对象，通过这个对象可以获取协程的返回值，
#           如果回调函数需要多个参数，可以通过偏函数导入。

from functools import partial


def func(a, b):
    return a + b


# 正常使用
result = func(1, 2)

# 使用偏函数导入一个参数，返回一个新函数
new_func = partial(func, 1)  # 相当于把原函数中的第一个参数a固定一个值为1，新函数只需要传入一个参数b即可
result2 = new_func(2)

print(result, result2)
