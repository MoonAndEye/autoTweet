# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:08:04 2016

"""
import pandas as pd
import numpy as np
import time
import datetime
import matplotlib as plt
import random as rd

time_axis = []

"""
三個小時半的交易, 就是270 min
"""


startTime = "09:01"
startPoint = 8832.42
singleRange = startPoint * 0.1
singleRange = int(singleRange)
"""
singleRange 是單邊範圍,到時候可以下一個random(singleRange, singleRange * -1)
"""

timeIndex = pd.date_range(startTime, periods = 270, freq="min")

predict = pd.DataFrame(np.random.randn(len(timeIndex)), columns=["twStock"], index = timeIndex)

print(len(timeIndex))

min_index = []
min_index.append(startPoint)


for each_min in range(len(timeIndex) -1):
    init = min_index[each_min]
    nextPoint = init + rd.randint(int(-singleRange), singleRange)
    min_index.append(nextPoint)    

"""
這樣子失敗了,因為不斷的相加,不斷的減少,很容易就會超過上下限
怎麼辦?
我要怎麼模擬,台股有上下限的
所以,改成 while loop ?
只要長度和 timeIndex 沒有 match, 就不斷的產生一個數字
而只有這個數字在限制的


換個想法

一開始丟出一個上限,和一個下限

然後 random 的東西就直接設定在這區間,就不會超過啦
"""
