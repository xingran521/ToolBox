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
    判断文件是否存在
"""
class File(object):

    def __init__(self, path, typen = "", data = "", Read_write = "r", Recursive = "False", No_scan_path = []):
        """数据传入

        Args:
            path (_type_, optional): 文件或文件夹路径.
            typen (str, optional): 文件类型.
            data (str, optional): 保存文件的数据. Defaults to "".
            Read_write (str, optional): 是读取还是写入(r读取w写入). Defaults to "r".
            Recursive (str, optional): 是否递归文件识别. Defaults to "False".
            No_scan_path (str, optional): 不扫描路径，递归执行填写参数. Defaults to [].
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
        # 不扫描路径或文件
        self.no_path = No_scan_path

    # json文件识别
    def js(self):
        """
        备注：未写写入
        Returns:
            _type_: 返回识别数据
        """
        # 打开文件并储存
        File_data = open(self.path, self.Read_write ,encoding='utf8')
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

    # txt文件识别
    def txt(self):
        # 打开文件并储存
        File_data = open(self.path, self.Read_write ,encoding='utf8')
        # 直接将文件中按行读到list里，效果与方法2一样
        data = File_data.readlines()  
        # 关
        File_data.close()  
        #返回list
        return data 

    # 自动递归识别
    def Recursive_identification(self, dir_path, list_name = []):
        """递归识别文件+路径

        Args:
            dir_path (_type_): 文件夹路径，必传参数.
            list_name (list, optional): 递归返回参数. Defaults to [].

        Returns:
            _type_: 返回list_name
        """
        # 获取文件（夹）名
        for file in os.listdir(dir_path):
            # 将文件（夹）名补全为路径
            file_path = os.path.join(dir_path, file)
            # 拒绝递归的文件以及文件路径
            if (file in self.no_path or file_path in self.no_path):
                pass
            # 如果是文件夹，则递归
            elif(os.path.isdir(file_path) == True and file != ""):
                self.Recursive_identification(file_path)
            else:
                # 保存路径
                list_name.append(file_path)
        return list_name


    # 主方法
    def main(self):
        """
        备注：未写自动识别
        Returns:
            _type_: 返回处理数据
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
            if (self.type == "txt"):
                return self.txt()
        else:
            # 启动文件递归
            return self.Recursive_identification(dir_path = self.path)
