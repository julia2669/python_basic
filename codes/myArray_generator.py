#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author : Julia
# @Version：V 0.1
# @File : generator.py
# @desc :
import time


def fab(maxn):
    n, a, b = 0, 0, 1
    while n < maxn:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)


def arrayWindow(arr, x):
    i = 0
    while x + i < len(arr):
        list = arr[i:i + x]
        i = i + 1
        yield list


print()
a = [i for i in range(0, 10)]

star = time.time()
for i in arrayWindow(a, 2):
    if i[0] % 1000 == 0:
        print(i)
end = time.time()
print(star - end)
print(int(4 / 2))
