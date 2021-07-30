#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 16:00 
# @Author : Julia
# @Version：V 0.1
# @File : coroutine_asyncio2.py
# @desc :   isinstance() 与 type() 区别：
#                   type() 不会认为子类是一种父类类型，不考虑继承关系。
#                   isinstance() 会认为子类是一种父类类型，考虑继承关系。

import asyncio

async def work(x):# 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running...'.format(x))
coroutine_2 = work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine_2)
# task = asyncio.ensure_future(coroutine_1)  # 这样也能创建一个task
print(task)
loop.run_until_complete(task)# run_until_complete接受的参数是一个future对象，当传入一个协程时，其内部自动封装成task
print(task)
print(isinstance(task,asyncio.Future))
