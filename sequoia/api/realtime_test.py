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


if __name__ == '__main__':
    pass
