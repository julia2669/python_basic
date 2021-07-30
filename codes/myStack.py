#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author : Julia
# @Version：V 0.1
# @File : myStack.py
# @desc :

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.toplist =[]
        self.buttomlist=[]


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.toplist.append(x)
        if len(self.toplist) > 1:
            x = self.toplist.pop(0)
            self.buttomlist.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.toplist)<1 and len(self.buttomlist)>0:
            x = self.buttomlist.pop()
            self.toplist.append(x)
        return self.toplist.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.toplist)<1 and len(self.buttomlist)>0:
            x = self.buttomlist.pop()
            self.toplist.append(x)
        return self.toplist[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.toplist)==0&len(self.buttomlist)==0



from collections import deque


class MyStackdq:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q2[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q2



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(6)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()


obj2 = MyStackdq()
obj2.push(5)
obj2.push(6)
param_2 = obj2.pop()
param_3 = obj2.top()
param_4 = obj2.empty()