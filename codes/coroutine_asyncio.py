#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 12:38 
# @Author : Julia
# @Version：V 0.1
# @File : coroutine_asyncio.py
# @desc :
'''
1、event_loop 事件循环：相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足条件时，就会调用对应的处理方法。
2、coroutine 协程：协程对象，只一个使用async关键字定义的函数，他的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环中，由事件循环调用。
3、task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程的进一步封装，其中包含任务的各种状态。
4、future：代表将来执行或没有执行的任务结果。它与task没有本质的区别。
5、async/await 关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
'''

import asyncio

async def work(x):# 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running...'.format(x))

coroutine_1 = work(1)# 协程是一个对象，不能直接运行

# 方式一：
loop = asyncio.get_event_loop() #创建一个事件循环
result = loop.run_until_complete(coroutine_1)# 将协程对象加入到事件循环中，并执行
print(result)# 协程对象并没有返回结果，打印None

# ------------------------------------------------------------------------------------------

# 方式二：
# asyncio.run(coroutine_1)  #创建一个新的事件循环，并以coroutine_1为程序的主入口，执行完毕后关闭事件循环
async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main())# 在事件循环中只有一个协程，所以没有挂起任务执行其他任务这一过程
# 运行结果先打印hello然后等待1秒打印world



