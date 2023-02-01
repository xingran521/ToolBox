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

def js():
    print (os.getcwd())
    f = open(os.getcwd()+'\libs\config\cs.json', 'r')
    content = f.read()
    a = json.loads(content)
    print(type(a))
    print(a)
    f.close()