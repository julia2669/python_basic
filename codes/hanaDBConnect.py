#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/13/2021 16:48 
# @Author : Julia
# @Version：V 0.1
# @File : hanaDBConnect.py
# @desc :
# pip install pyhdb
import pyhdb

def get_connection():
    conn_obj = pyhdb.connect(
        host="10.33.67.12",
        port=30015,            #多租户的端口需要准确的如30053，
        user="***",
        password="***"
    )

    return conn_obj


def get_employees(conn,A):
    cursor = conn.cursor()
    #cursor.execute("select * from XMZX.ZTEST_HANA where ID='a' ")  #python官方例子的SQl模式，去掉字段和表的双引号
    cursor.execute("select * from XMZX.ZTEST_HANA where ID='%s' "%(A))# 传递参数到
    #cursor.execute('select "ID","NAME","ZCLNT" from "XMZX"."ZTEST_HANA" where "ID"=\'a\' ')　＃HANA生成的ＳＱＬ需将'转义
    employees = cursor.fetchall()
    conn.close()
    return employees


if __name__=='__main__':
    conn = get_connection()
    employees = get_employees(conn,'b')
    for employee in employees:
        print (employee)