# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : File.py
@version : 1.0
@Time    : 2023/02/01 10:16:10
@Author  : cxr
@Desc    : 文件操作
'''

# 导入库
import json,os
""" 主函数 """
class File(object):
    def __init__(self):
        self.path = os.getcwd()+'\libs\config\cs.json'
        print (self.path)

    # json文件识别
    def js(self):
        f = open(self.path, 'r')
        content = f.read()
        a = json.loads(content)
        print(type(a))
        print(a)
        f.close()

    