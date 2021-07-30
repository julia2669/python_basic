#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/26/2021 15:14 
# @Author : Julia
# @Version：V 0.1
# @File : operate_yaml.py
# @desc :、大小写敏感
# 、使用缩进表示层级关系
# 、缩进时不允许使用Tab键，只允许使用空格。
# 、缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
# 、# 表示注释，从这个字符一直到行尾，都会被解析器忽略，这个和python的注释一样6、列表里的项用"-"来代表，字典里的键值对用":"分隔

import yaml

yaml_str = """
name: 一条大河
age: 1956
job: Singer
"""

y = yaml.load(yaml_str, Loader=yaml.SafeLoader)
print(y)
import datetime
import pytz

yaml_data = {
    "str": "Big River",
    "int": 1548,
    "float": 3.14,
    'boolean': True,
    "None": None,
    'time': datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat(),
    'date': datetime.datetime.today()
}

with open('./yaml_test', 'w') as f:
    y = yaml.dump(yaml_data, f)
    print(y)

with open('./yaml_test', 'r') as r:
    y1 = yaml.load(r, Loader=yaml.SafeLoader)
    print(y1)