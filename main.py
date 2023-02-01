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
from libs.Welcome import *
from libs.File import *

"""主体"""
class ToolBox(object):
    # 函数数据变量初始化方法
    def __init__(self):
        pass
    # ...
    def Welcome(self):
        pass
    # 主方法
    def main(self):
        holle()
        File().main()

if __name__ in "__main__":
    ToolBox().main()