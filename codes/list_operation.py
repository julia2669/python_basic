#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author : Julia
# @Version：V 0.1
# @File : listOperation.py
# @desc :

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list3 = []          ## 空列表
list3.append('Google')   ## 使用 append() 添加元素
list3.append('Runoob')
del list1[2]
print(list1,list2,list3)
a=[1, 2, 3] + [4, 5, 6]
print(a) #[1, 2, 3, 4, 5, 6]
print(['Hi!'] * 4) #['Hi!', 'Hi!', 'Hi!', 'Hi!']

# print(cmp(list1, list2)) Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象
# 你可以用表达式 (a > b) - (a < b) 代替 cmp(a,b)
seq = (1,2,3,'aaa')
t = list(seq)
print(len(t),max(list3),min(list3),t)
list1.append('1997')# 在列表末尾添加新的对象
list1.count(1997)# 统计某个元素在列表中出现的次数
list1.extend(seq)#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1.index(1)#从列表中找出某个值第一个匹配项的索引位置
list1.insert(1, 'obj')#将对象插入列表
listpop = list1.pop(-1)#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1.remove('obj')#移除列表中某个值的第一个匹配项
list1.reverse()#反向列表中元素
# list1.sort(cmp=None, key=None, reverse=False)
print(list1,listpop)
print(max(a))


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序降序
random.sort(key=takeSecond,reverse=True)
# 输出类别
print('排序列表：')
print(random)
