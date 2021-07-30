#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author : Julia
# @Version：V 0.1
# @File : collectionQ.py
# @desc :
'''在FIFO队列中，按照先进先出的顺序检索条目。
在LIFO队列中，最后添加的条目最先检索到（操作类似一个栈）。
在优先级队列中，条目被保存为有序的（使用heapq模块）并且最小值的条目被最先检索。'''

import queue
import time

def queue_q():
    q = queue.Queue(5)
    #FIFO队列先进先出 first in first out
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    # q.put(3) 阻塞直到有queue有空位
    q.get()  #1 will be get and poped
    q.put(6)

    while not q.empty():
        next_item = q.get()
        print(next_item)
        time.sleep(1)

    print('---'*10)

def queue_Lifoq():
    q = queue.LifoQueue()
    #LIFO队列后进先出 last in first out
    q.put(1)
    q.put(2)
    q.put(3)

    while not q.empty():
        next_item = q.get()
        print(next_item)
    print('---'*10)

def queue_priorityq():
    from queue import PriorityQueue
    import time

    q = PriorityQueue()
    #它一般通过堆这一数据结构，而堆其实是一种完全二叉树，它会对进入容器的元素进行排序（根据事先指定的规则），出队的顺序则会是二叉树的根结点代表的元素
    q.put((2, 'code'))
    q.put((1, 'eat'))
    q.put((3, 'sleep'))

    while not q.empty():
        next_item = q.get()
        print(next_item)
        time.sleep(3)


    q.qsize()
    q.empty()
    q.full()
    q.put('item', block=True, timeout=None)
    #如果block是True，且timeout是None，该方法将一直等待直到有队列有空余空间
    # (默认block=True,timeout=None)。如果timeout是一个正整数，该方法则最多阻塞timeout秒并抛出Full异常。
    # 如果block是False并且队列满，则直接抛出Full异常（这时timeout将被忽略）。

def collecotions_q():
    import collections
    q = collections.deque([1, 2, 3, 4])
    print(5 in q)  # False
    print(1 in q)  # True
    # 顺时针
    q.rotate(1)
    print(q)  # [4, 1, 2, 3]
    q.rotate(1)
    print(q)  # [3, 4, 1, 2]
    # 逆时针
    q = collections.deque([1, 2, 3, 4])
    q.rotate(-1)
    print('# 逆时针',q)  # [2, 3, 4, 1]
    q.rotate(-1)
    print(q)  # [3, 4, 1, 2]
    d=collections.deque()
    d.append(1)
    d.append(2)
    print('append 2 add to backend',d)
    d.appendleft(9)
    print('appendleft 9 add to front',d)
    print('pop front element',d.pop())
    print('popleft pop back element',d.popleft())
    d1 = d.copy()
    print(d1)
    d.clear()
    d.append(1)
    d.extend([3,4,5])
    print(d)
    d.clear()
    d.append(1)
    d.extendleft([3,4,5])
    print(d)
    d.clear()
    d.extend(["a","b","c","d","e","f"])
    print(d)
    print(d.index("c",0,4))
    # print(d.index("c", 0, 2)) ## ValueError: 'c' is not in deque

    c = collections.deque(maxlen=3)
    c.append(0)
    x=[1,2]
    c.append(x)
    # 指定队列的长度后，如果队列已经达到最大长度，此时从队尾添加数据，则队头的数据会自动出队。
    # 队头的数据相等于被队尾新加的数据“挤”出了队列，以保证队列的长度不超过指定的最大长度。反之，从队头添加数据，则队尾的数据会自动出队
    print(c)
    c.append(4)
    print(c)

    c.count(c)
    c = collections.deque(maxlen=3)
    x=[1,2,3,4,5]
    c.extend(x)
    c.extendleft(x)
    print(c)
    c.count(c)
    print('len(d),c.maxlen:',len(d),c.maxlen)
    print(d.popleft())

collecotions_q()

