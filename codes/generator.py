#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 11:27 
# @Author : Julia
# @Version：V 0.1
# @File : generator.py
# @desc :

def generator():
    i=0
    while i<5:
        print("我在这。。。")
        xx=yield i ## python 程序，碰到=都是先从右往左执行
        print(xx)
        i+=1

g=generator()
g.send(None)        # <==> next(g)第一次启动，执行到yield i（此时i=0），挂起任务，主程序继续往下执行
g.send("lalala")    #第二次唤醒生成器，从上次的yield i处继续执行，即往左执行，把lalala赋值给xx后，
                    # 往下执行，直到下次的yield i（此时i=1），挂起任务
# next(g) #<==>g.__next__()不常用

# -------------------------------------------------------------------------------------------
# 生产者消费者模型
def consumer():
    print('--4. 开始执行生成器代码--')
    response =None
    while True:
        print('--5. yield, 中断，保存上下文--')
        n = yield response # yield, 中断， 保存上下文
        print('--8.获取上下文，继续往下执行--')
        if not n:
            return
        print("[Consumer]: consuming {}..".format(n))
        response = "OK"

def producer(c):
    print("--3.启动生成器，开始执行生成器consumer--")
    c.send(None) #3.启动生成器，开始执行生成器consumer
    print('--6.继续往下执行--')
    n=0
    while n<5:
        n+=1
        print("[Producer]: producing {}..".format(n))
        print("--7. 第{}次唤醒生成器，从yield位置继续往下执行！--".format(n+1))
        r=c.send(n) #第二次唤醒生成器
        print("--9. 从第8步往下--")
        print("[Producer]: consumer return {}..".format(r))
    c.close()

if __name__=="__main__":
    c=consumer() #1.定义生成器，consumer并不执行
    producer(c) # 2. 运行producer 函数

