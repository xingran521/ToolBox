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
        # 作者名字
        self.name = self.info["name"]
        # 邮箱
        self.mail = self.info["mail"]
        # 版本
        self.version = self.info["version"]
        # 取出info->Display->Sentence->随机
        self.Content = self.info["Display"]["Sentence"][str(random.randint ( 0, len(self.info["Display"]["Sentence"])-1))]
    
    # 欢迎方法
    def holle(self):
        # 调用数据处理
        self.Data_Handling()
        # 信息拼接展示
        print("-"*80)
        # logo
        print("'\n'  $$$$$$$$\                     $$\ $$$$$$$\                      \n'  \__$$  __|                    $$ |$$  __$$\                     \n'     $$ |    $$$$$$\   $$$$$$\  $$ |$$ |  $$ | $$$$$$\  $$\   $$\ \n'     $$ |   $$  __$$\ $$  __$$\ $$ |$$$$$$$\ |$$  __$$\ \$$\ $$  |\n'     $$ |   $$ /  $$ |$$ /  $$ |$$ |$$  __$$\ $$ /  $$ | \$$$$  / \n'     $$ |   $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ | $$  $$<  \n'     $$ |   \$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |\$$$$$$  |$$  /\$$\ \n'     \__|    \______/  \______/ \__|\_______/  \______/ \__/  \__|\n'")
        # 关于
        print("'\t\t\t\t\t\tholle {} open TooBox by xingran")
        print("-"*80)
        
    # 主方法
    def main(self):
        self.holle()
