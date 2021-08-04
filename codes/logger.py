#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 8/4/2021 10:15 
# @Author : Julia
# @Version：V 0.1
# @File : logger.py
# @desc :
import logging
import logging.handlers
import os
import functools
from datetime import datetime

class Logger():
    loggers={}

    @staticmethod
    def prepare_logger(logger=None, logname=__name__, loglevel=logging.INFO,logto = None):
        if logger is None:
            if logto is None:
                lh = logging.StreamHandler()
            else:
                logdir = os.path.dirname(logto)
                if not os.path.exists(logdir):os.makedirs(logdir)
                lh = logging.handlers.TimedRotatingFileHandler(logto,when='d',backupCount=10)

            formatter = logging.Formatter('[%(asctime)s][%(module)s][%(funcName)s][%(levelname)s]%(message)s','%m-%d %H:%M:%S')
            lh.setFormatter(formatter)
            lh.setLevel(loglevel)

            #prepare logger
            new_logger = logging.getLogger(logname)
            if logname not in Logger.loggers:
                Logger.loggers[logname]=1
                new_logger.setLevel(loglevel)
                new_logger.addHandler(lh)

        else:
            new_logger =logger

        return new_logger