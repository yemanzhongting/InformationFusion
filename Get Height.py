# -*- coding: utf-8 -*-
# @Time    : 2022/1/15 19:53
# @Author  : yemanzhongting
# @Email   : sggzhang@whu.edu.cn
# @File    : Get Height.py
# @Software: PyCharm
import configparser
import os, sys

parent_dir = os.path.dirname(os.path.abspath(__file__))

#  实例化configParser对象
config = configparser.ConfigParser()
config.read(parent_dir + "/config.init", encoding='utf-8')  # 读取配置文件采用绝对路径

if __name__ == '__main__':