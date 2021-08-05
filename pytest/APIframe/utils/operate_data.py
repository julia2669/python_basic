#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/27/2021 11:48 
# @Author : Julia
# @Version：V 0.1
# @File : operate_csv.py
# @desc :
        # d= df.to_dict() #{column: {index: value}} default
        # d = df.to_dict(orient='list')  #{column: [values]}
        # d = df.to_dict(orient='series') #{column: Series(values)}
        # d = df.to_dict(orient='index') # {index: {column: value}}


from utils.helper import *
import pandas as pd
import yaml
import json

class OperateData():
    def dic_to_list(self, data):
        '''
        convert a dic values to list
        :param data: dic
        :return: list
        '''
        self.li=[]
        for i in data:
            self.li.append(data[i])
        return self.li

    def read_csv(self,filedir,file):
        '''
        :param filedir:  file dir under the project
        :param file: file name
        :return: a list with formate: [{column: value,column: value},{column: value,column: value}]
        '''
        df = pd.read_csv(FilePath(filedir,file))
        df = df.to_dict(orient='index')
        df = self.dic_to_list(df)
        return df

    def read_excel(self, filedir, file, sheet_name=[0]):
        '''
        :param filedir:  file dir under the project
        :param file: file name
        :param sheet_name: str, int, list, or None, default 0
                            sheet name need to retrive values, can use sheet name or index
        :return: a dict contains all sheets data, formats as blow:
                {'sheet0':
                        {index: {column: value}}
                'sheet1':
                        {index: {column: value}}
                }
        '''
        df = pd.read_excel(FilePath(filedir,file),sheet_name=sheet_name)
        for i in df:
            df[i]=df[i].fillna('None').to_dict(orient='index')
            df[i] = self.dic_to_list(df[i])
            # print(df[i].T)
        df = self.dic_to_list(df)
        return df

    def readMultiYaml(self,filedir, file):
        '''
        :param filedir:  file dir under the project
        :param file: file name
        :return: a list of data
        '''
        with open(FilePath(filedir,file),encoding='utf-8') as fp:
            return list(yaml.safe_load_all(fp))

    def readYaml(self,filedir, file):
        with open(FilePath(filedir,file),encoding='utf-8') as fp:
            return yaml.safe_load(fp)

    def writeYaml(self,filedir, file,content,mode):
        with open(FilePath(filedir, file),mode=mode,encoding='utf-8') as fp:
            yaml.dump(content,fp)

    def readJson(self,filedir, file):
        with open(FilePath(filedir, file), encoding='utf-8') as fp:
            return json.load(fp)


# od=OperateData()
# case = od.read_csv('data','todo.csv')
# print(case)
# case_excel = od.read_excel('data','todo.xlsx')
# print(case_excel)
# case_excel2 = od.read_excel('data','todo.xlsx',sheet_name=['ToDoApp','BookApp'])
# print(type(case_excel2))
# for i in case_excel2:
#     for j in i:
#         print(j)
# case_yaml = od.readYaml('data','todo.yaml')
# print(type(case_yaml))
# print(case_yaml)
# yamls=od.readMultiYaml('data','yaml_example.yaml')
# for i in yamls:
#     print(i)
# print(od.readJson('data','json_example.json'))
# s=[[1,4],[2,3]]
# od.writeYaml('data','temp.yaml',s,'w')
