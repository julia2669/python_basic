#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/21/2021 16:42 
# @Author : Julia
# @Version：V 0.1
# @File : f_strings.py
# @desc :   In Python 3.6, the f-string was introduced(PEP 498).
#           In short, it is a way to format your string that is more readable and fast.


agent_name = 'James Bond'
kill_count = 9

# old ways
print('{0} has killed {1} enemies '.format(agent_name,kill_count))
print('{0} has killed {1} enemies '.format(agent_name,kill_count * 100))

# f-strings way
print(f'{agent_name} has killed {kill_count} enemies')
print(f'{agent_name} has killed {kill_count * 100} enemies')
