#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author : Julia
# @Version：V 0.1
# @File : BitOperation.py
# @desc :

#十进制转换为二进制、八进制、十六进制
a =bin(23)
print(a)  # '0b10111'
b = oct(23)
print(b)  #'0o27'
c = hex(23)
print(c)  # '0x17'

# 直接反向获取十进制
print(0b10111)#23
print(0o27)#23
print(0x17)#23

# 用int函数来转换
print(int('0b10111', 2))#23
print(int('0o27', 8))#23
print(int('0x17', 16))#23

'''
& 按位与:  全1才1否则0 :只有对应的两个二进位均为1时,结果位才为1,否则为0
| 按位或:  有1就1 只要对应的二个二进位有一个为1时,结果位就为1,否则为0
^ 按位异或: 不同为1 当对应的二进位相异(不相同)时,结果为1,否则为0
~ 按位取反
<< 按位左移:  各二进位全部左移n位,高位丢弃,低位补0 
            x << n 左移 x 的所有二进制位向左移动n位,移出位删掉,移进的位补零
                a. 左移1位相当于 乘以2
                用途:快速计算一个数乘以2的n次方 (8<<3 等同于8*2^3)
                b.左移可能会改变一个数的正负性
>> 按位右移:  各二进位全部右移n位,保持符号位不变
            x >> n x的所有二进制位向右移动n位,移出的位删掉,移进的位补符号位 右移不会改变一个数的符号
                右移1位相当于 除以2
                x 右移 n 位就相当于除以2的n次方 用途:快速计算一个数除以2的n次方 (8>>3 等同于8/2^3)
'''
big =2

medium=2
small=2
cnt=0
for i in range(30):
    cur = 0
    if (i < 10) :
        cur = (big >> i) & 1
        print(cur)
        print(cnt)
    elif (i < 20) :
        cur = (medium >> (i - 10)) & 1
    elif (i < 30) :
        cur = (small >> (i - 20)) & 1
    cnt=cur+1
    if cnt == 1:
        1<<i
    else:
        cnt=0





