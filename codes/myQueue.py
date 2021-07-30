#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author : Julia
# @Version：V 0.1
# @File : myQueue.py
# @desc :

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.outqueue = []
        self.inqueue = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inqueue.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outqueue) == 0:
            self.outqueue=self.inqueue
        x = self.outqueue[0]
        del self.outqueue[0]
        return x



    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.outqueue[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.inqueue) > 0 or len(self.outqueue) > 0:
            return False
        else:
            return True



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2,param_3,param_4)