#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project :my_sequoia
@FileName:realtime_test
@Python  :PyCharm
@Author  :Sunny
@Time    :2022/9/22 17:15
@Desc    :实时测试模型
=================================================="""
import os
import time
import pandas as pd


def read_local():
    """
    读取1min历史行情，进行测试
    """
    file_cache = "D:\\data\\history_rb#FT_2022-01-01_60s_1.feather"
    rb_main = pd.read_feather(file_cache)

    return rb_main


def loop_bar():
    """
    遍历播放历史bar数据
    :return:
    """
    rb_bar = read_local()
    for i in range(len(rb_bar)):
        print(rb_bar.iloc[i])


if __name__ == '__main__':
    loop_bar()
