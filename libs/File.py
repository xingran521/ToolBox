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
"""缺少读取加载
"""
class File(object):

    def __init__(self, path, typen, data = "", Read_write = "r", Recursive = "False"):
        """数据传入

        Args:
            path (_type_, optional): 文件或文件夹路径.
            typen (str, optional): 文件类型.
            data (str, optional): 保存文件的数据. Defaults to "".
            Read_write (str, optional): 是读取还是写入(r读取w写入). Defaults to "r".
            Recursive (str, optional): 是否递归文件识别. Defaults to "False".
        """
        # 路径
        self.path = path
        # 是否自动识别递归路径以及名字
        self.Recursive = Recursive
        # 文件类型
        self.type = typen
        # 读取写入
        self.Read_write = Read_write
        # 数据
        self.data = data

    # json文件识别
    def js(self):
        """
        备注：未写写入
        Returns:
            _type_: _description_
        """
        # 打开文件并储存
        File_data = open(self.path, self.Read_write)
        # 逐个字符读取
        content = File_data.read()
        # print(content)
        # 判断读写
        if(self.Read_write == "w"):
            pass            
        else:
            # 返回转化成Python数据
            return json.loads(content)

        # 退出打开数据
        File_data.close()

    # 自动递归识别
    def Recursive_identification(self):
        pass

    # 主方法
    def main(self):
        """
        备注：未写自动识别
        Returns:
            _type_: _description_
        """
        # 判断路径是否有写
        if (self.path == False):
            print("路径没写是<(＿　＿)>")
            return 0 
        # 判断是否自动识别
        if (self.Recursive == "False"):
            # 判断类型
            if (self.type == "json"):
                return self.js()
        else:
            print("自动识别")
    