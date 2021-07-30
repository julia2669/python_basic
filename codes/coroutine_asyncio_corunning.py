#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 12:38 
# @Author : Julia
# @Version：V 0.1
# @File : coroutine_asyncio.py
# @desc :并发运行任务的案例


import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
