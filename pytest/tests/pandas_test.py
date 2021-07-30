#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/26/2021 15:29 
# @Author : Julia
# @Version：V 0.1
# @File : pandas_test.py
# @desc :

import pandas as pd

print(pd.__version__)
print('--'*30)
data = [['Google',10],['Runoob',12],['Wiki',13]]

df = pd.DataFrame(data,columns=['Site','Age'],dtype=float)

print(df)
print('--'*30)
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df = pd.DataFrame(data)

print (df)
print('--'*30)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

df = pd.DataFrame(data)

print (df)
print('--'*30)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
print(df)
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
print('--'*30)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行和第二行
print(df.loc[[0, 1]])

print('--'*30)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

print('--'*30)
df = pd.read_csv('nba.csv')

# print(df.to_string())  #to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
print(df)

# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

# 字典
dict = {'name': nme, 'site': st, 'age': ag}

df2 = pd.DataFrame(dict)

# 保存 dataframe
df2.to_csv('site.csv')
print('--'*30)
print(df.head())#head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。
print('--'*30)
print(df.tail(3)) #tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。
print('--'*30)
print(df.info())



