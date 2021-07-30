#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 16:00 
# @Author : Julia
# @Version：V 0.1
# @File : coroutine_asyncio2.py
# @desc : 在task执行完毕的时候可以获取执行的结果，回调的最后一个参数是future对象，通过这个对象可以获取协程的返回值，
# 如果回调函数需要多个参数，可以通过偏函数导入。从下例可以看出，coroutine执行结束时候会调用回调函数，
# 并通过future获取协程返回（return）的结果。我们创建的task和回调里面的future对象，实际上是同一个对象。

import asyncio

async def work(x):# 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running...'.format(x))
    return "Work {} is finished".format(x)

def call_back(future):
    print("Callback:{}".format(future.result()))

coroutine_2 = work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine_2)  # 这样也能创建一个task
task.add_done_callback(call_back)
loop.run_until_complete(task)# run_until_complete接受的参数是一个future对象，当传入一个协程时，其内部自动封装成task
print(task)
