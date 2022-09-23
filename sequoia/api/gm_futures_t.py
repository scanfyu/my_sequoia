#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project :my_sequoia
@FileName:gm_futures_t
@Python  :PyCharm
@Author  :Sunny
@Time    :2022/9/23 12:27
@Desc    :配合 CzscAdvancedTrader 在掘金进行期货测试
=================================================="""
import inspect
import traceback
from czsc.gms.gm_base import *
from czsc.objects import PositionLong, PositionShort, Operate


object_futures = {
    "螺纹主力": 'SHFE.RB',
}


def on_bar(context, bars):
    """订阅K线回调函数"""
    context.unfinished_orders = get_unfinished_orders()
    # 撤销挂单时间超过 30 分钟的订单。
    cancel_timeout_orders(context, max_m=30)


def report_account_status(context):
    """报告账户持仓状态"""
    # 周末状态
    if context.now.isoweekday() > 5:
        return
