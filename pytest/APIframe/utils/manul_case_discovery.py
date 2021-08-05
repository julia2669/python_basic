#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 8/5/2021 13:45 
# @Author : Julia
# @Version：V 0.1
# @File : manul_case_discovery.py
# @desc :

from utils.operate_data import OperateData

od = OperateData()
read_excel = od.read_excel('data','LIFI_Intergration Test Case for TPS.xlsx',['TestCase'])
for i in read_excel[0]:
    print(i.get('Steps'))
    print('-----'*20)