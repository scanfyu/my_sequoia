#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project :my_sequoia
@FileName:bar_1m_base
@Python  :PyCharm
@Author  :Sunny
@Time    :2022/9/23 10:39
@Desc    :1分钟线的技术面分析
=================================================="""
from sequoia.api.realtime_test import read_local
from czsc import CZSC
from czsc.gms.gm_base import format_kline
from czsc.enum import Freq
import pandas as pd
import numpy as np


def kline_raw_bar(df_slice):
    bars = format_kline(df_slice, freq=Freq.F1)
    return bars


def loop_bar():
    """
    播放历史bar数据
    :return:
    """
    rb_bar = read_local()
    for i in range(len(rb_bar)):
        # 轮询播放bar数据
        raw_bars = kline_raw_bar(rb_bar.iloc[i:i+1])

        c = CZSC(raw_bars)

        # 1.衍生多周期数据；2.笔的划分
        # 实时的数据传进来，丢到数据流里建模


if __name__ == '__main__':
    loop_bar()
