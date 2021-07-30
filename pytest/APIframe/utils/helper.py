#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/27/2021 11:57 
# @Author : Julia
# @Version：V 0.1
# @File : helper.py
# @desc :重构公共工具类方法

import os
import logging
import datetime

def FilePath(filePath=None, fileName=None):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), filePath,fileName)

def log(log_content):
    logFile = logging.FileHandler(FilePath('log','logInfo.md'), 'a', encoding='utf-8')
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
    logFile.setFormatter(fmt)

    logger1 = logging.Logger('logTest', level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)
    logFile.close()



# print(FilePath('utils','helper.py'))
# print(log('test log'))