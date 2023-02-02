# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : holle.py
@version : 1.0
@Time    : 2023/02/01 11:32:13
@Author  : cxr
@Desc    : 欢迎加载
'''

# 导入库
from libs.File import *
import random

class Welcome(object):
    # 传参方法
    def __init__(self) -> None:
        self.info = File(os.getcwd()+'\libs\config\info.json',"json").main()
    
    # 数据处理
    def Data_Handling(self):
        print(self.info["name"])
        print(self.info["mail"])
        print(self.info["version"])
        print(self.info["Display"]["Sentence"][str(random.randint ( 0, len(self.info["Display"]["Sentence"])-1))])
        nu = random.randint ( 0, len(self.info["Display"]["Sentence"])-1)
    
    # 欢迎方法
    def holle(self):
        # 调用数据处理
        self.Data_Handling()
        # 信息拼接展示
        print("-"*50)
        print("ToolBox")
        print("holle {} open TooBox by xingran")
        print("-"*50)
        
    # 主方法
    def main(self):
        self.holle()
