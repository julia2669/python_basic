#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 12:16 
# @Author : Julia
# @Version：V 0.1
# @File : coroutine_greenlet.py
# @desc : greenlet已经实现了协程，但是这个需要人工切换，很麻烦。
import time
from greenlet import greenlet


def task_1():
    while True:
        print("--This is task1!--")
        g2.switch()  # 切换到g2中运行
        time.sleep(0.5)


def task_2():
    while True:
        print("--This is task 2!--")
        g1.switch()  # 切换到g1中运行
        time.sleep(0.5)


if __name__ == "__main__":
    g1 = greenlet(task_1)
    g2 = greenlet(task_2)
    g1.switch()
