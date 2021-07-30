#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 12:24 
# @Author : Julia
# @Version：V 0.1
# @File : gevent.py
# @desc :   能够自动切换任务的模块gevent，其原理是当一个greenlet遇到IO(比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的greenlet，
#           等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程 ，
#           就保证总有greenlet在运行，而不是等待IO。
#           monkey补丁 不必强制使用gevent里面的sleep、sorcket等等了


import gevent
from gevent import monkey
import random
import time

def task_1(num):
    for i in range(num):
        print(gevent.getcurrent(),i)
        gevent.sleep(1) #模拟一个耗时操作，注意不能使用time模块的sleep

def task_2(name):
    for i in range(3):
        print(name,i)
        time.sleep(1)

def task_3(name):
    for i in range(3):
        print(name,i)
        time.sleep(1)

if __name__ == "__main__":
    g1 = gevent.spawn(task_1,5) #创建协程
    g2 = gevent.spawn(task_1,5)
    g3 = gevent.spawn(task_1,5)
    g1.join()#等待协程运行完毕
    g2.join()

    monkey.patch_all()# 给所有的耗时操作打上补丁
    gevent.joinall([  # 等到协程运行完毕
        gevent.spawn(task_2,"task_2"), # 创建协程
        gevent.spawn(task_3, "task_3")
    ])
    print("the main thread")