#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 16:00 
# @Author : Julia
# @Version：V 0.1
# @File : coroutine_asyncio2.py
# @desc : 当回调函数需要传递多个参数时
import asyncio
from functools import partial

async def work(x):# 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running...'.format(x))
    return "Work {} is finished".format(x)

def call_back(num, future):
    print("Callback:{}, the num is {}".format(future.result(), num))

coroutine_2 = work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine_2)  # 这样也能创建一个task
task.add_done_callback(partial(call_back,100))
loop.run_until_complete(task)# run_until_complete接受的参数是一个future对象，当传入一个协程时，其内部自动封装成task
print(task)
