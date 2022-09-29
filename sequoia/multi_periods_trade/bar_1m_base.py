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
import time


def kline_raw_bar(df_slice):
    bars = format_kline(df_slice, freq=Freq.F1)
    return bars


def loop_bar():
    """
    播放历史bar数据
    :return:
    """
    t1 = time.time()

    df_status = pd.DataFrame()
    n_close = 0

    # 读取本地的数据
    rb_bar = read_local()
    for i in range(len(rb_bar)):
        # 轮询播放bar数据
        raw_bars = kline_raw_bar(rb_bar.iloc[i:i + 1])
        raw_bar = raw_bars[-1]

        if i == 0:
            c = CZSC(raw_bars)
            n_return = 0
        else:
            c.update(raw_bar)
            n_return = np.log(n_close/raw_bar.close)

        # -- 特征值
        dt_ = raw_bar.dt
        # 最新价
        last_p = raw_bar.close
        # 单一bar涨跌幅
        r_d = (raw_bar.close / raw_bar.open - 1) * 100
        n_close = raw_bar.close
        # czsc对象
        # 未成笔的K线数量
        b_ubi = len(c.bars_ubi)
        # 成笔的数量
        b_lgh = len(c.bi_list)
        # 最新一笔的方向
        if b_lgh > 0:
            l_bi_dir = c.bi_list[-1].direction
            last_bi = c.bi_list[-1]
        else:
            l_bi_dir = "无"
            last_bi = None

        var_c = [last_p, dt_, r_d, n_return, b_ubi, b_lgh, l_bi_dir, last_bi]
        slice_t = pd.DataFrame(var_c).T

        df_status = pd.concat([df_status, slice_t])

    df_status.rename({"0": "price", "1": "time", "2": "b_pchg", "3": "pchg", "4": "ubi_n", "5": "bi_lg",
                      "6": "bi_dir", "7": "last_bi"})
    df_status.to_csv("D:/data/czsc_ana/rb_1m.csv")

    t_spend = time.time() - t1
    print(f"spend all {round(t_spend, 2)}, {round(t_spend/len(rb_bar), 5)} per once.")


if __name__ == '__main__':

    loop_bar()

