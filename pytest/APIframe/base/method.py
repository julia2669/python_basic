#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/27/2021 10:49 
# @Author : Julia
# @Version：V 0.1
# @File : method.py
# @desc :

import  requests

class Requests:
    def __init__(self):
        self.s = requests.Session()

    def request(self,url,method='get',**kwargs):
        if method =='put':
            if 'params' in kwargs:
                kwargs.get('params')['method']='put'
            else:
                kwargs['params']={'method':'put'}
            return self.s.request(url=url, method='post', **kwargs)
        else:
            return self.s.request(url=url,method=method,**kwargs)

    def get(self,url,**kwargs):
        return self.request(url=url,**kwargs)

    def post(self,url,**kwargs):
        return self.request(url=url,method='post',**kwargs)

    def put(self,url,**kwargs):
        return self.request(url=url,method='put',**kwargs)

    def delete(self,url,**kwargs):
        return self.request(url=url,method='delete',**kwargs)
