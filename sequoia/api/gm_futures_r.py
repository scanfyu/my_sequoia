#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project :my_sequoia
@FileName:gm_futures_r
@Python  :PyCharm
@Author  :Sunny
@Time    :2022/9/23 14:07
@Desc    :配合 CzscAdvancedTrader 在掘金进行实时期货测试
=================================================="""
import inspect
import traceback
from czsc.gms.gm_base import *
from czsc.objects import PositionLong, PositionShort, Operate


# 螺纹主力合约 1、5、10
object_futures = {
    "螺纹主力": 'SHFE.RB',
    "螺纹2201": 'SHFE.rb2201',
    "螺纹2205": 'SHFE.rb2205',
    "螺纹2210": 'SHFE.rb2210',
}

