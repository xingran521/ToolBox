# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : main.py
@version : 0.1
@Time    : 2023/02/01 09:59:35
@Author  : cxr
@Desc    : 工具集
'''

# 导入库
from libs import *

"""主体"""
class ToolBox(object):
    # 函数数据变量初始化方法
    def __init__(self):
        pass
    # 欢迎（可在后期尝试单独文件制作）
    def Welcome(self):
        print("-"*50)
        print("holle")
        print("-"*50)
    # 主方法
    def main(self):
        self.Welcome()

if __name__ in "__main__":
    ToolBox().main()