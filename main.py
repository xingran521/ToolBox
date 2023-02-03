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
    # 接收命令处理
    def Command_Handling(self):
        # 接收命令
        while True:
            # 输入命令判断
            Commands = input("cs>")
            # list工具列表
            if (Commands == "list"):
                pass
            # help帮助信息
            if (Commands == "help"):
                pass
            # open打开工具
            if (Commands == "open"):
                pass
            # exit退出程序
            if (Commands == "exit"):
                return 0

    # 主方法
    def main(self):
        # 欢迎
        Welcome().main()
        # 文件读取
        # File().main()
        
if __name__ in "__main__":
    ToolBox().main()