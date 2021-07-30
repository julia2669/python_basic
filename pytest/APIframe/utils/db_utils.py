#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/28/2021 10:38 
# @Author : Julia
# @Version：V 0.1
# @File : db_utils.py
# @desc :
import pymysql
import traceback


class MysqlTools():
    """
    连接mysql
    库、表操作
    """
    def __init__(self,host,dbname,user,passwd,charset="utf8"):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.passwd = passwd
        self.charset = charset


    def connectMysqlDatabase(self):
        """连接db"""
        try:
            #连接db
            connect = pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.dbname,charset=self.charset)
            cursor = connect.cursor()
            databaseConnectInfo = self.user + "@" + "self.host" + "/" +  self.dbname
            print("INFO:connect database %s success."%databaseConnectInfo)
            return connect,cursor
        except:
            traceback.print_exc()
            print("ERROR:FUNCTION connectMysqlDatabase connect mysql database failed.")


    def executeSqlLine(self,sqlLine):
        """执行单条sql语句"""
        if sqlLine and isinstance(sqlLine,str):
            print("INFO:now start connect mysql dababase.")
            connect,cursor = self.connectMysqlDatabase()
            executeResult = ""
            try:
                #游标执行sql
                cursor.execute(sqlLine)
                executeResult = cursor.fetchall()       #获取所有执行结果
                cursor.close()                          #关闭游标
                connect.commit()                        #确认提交
                print("INFO:execute sql sucess. sqlLine = ", sqlLine)
            except Exception as e:
                print("ERROR：execute sql failed.errorInfo =",e)
                print("ERROR:FUNCTION executeSql execute failed.sqlLine =",sqlLine)
                connect.rollback()                      #回滚db
                return str(e) + "    sqlLine = " + sqlLine
            #断开连接
            connect.close()
            print("INFO:connect closed.\n")
            return executeResult
        else:
            print("ERROR:param sqlLine is empty or type is not str.sqlLine = ",sqlLine)


    def executeBatchSql(self,sqlList):
        """
        批量执行sql
        exp:    executeBatchSql([sql_1,
                                sql_2,
                                sql_3,
                                ......
                                ])
        """
        finalResultList = []
        if sqlList:
            for sql in sqlList:
                executeResult = self.executeSqlLine(sql)
                finalResultList.append(executeResult)
        else:
            print("ERROR:param sqlList is empty.")
        return finalResultList