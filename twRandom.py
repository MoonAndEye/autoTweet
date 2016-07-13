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
singleRange = float('%.2f' %singleRange)
"""
singleRange 是單邊範圍,到時候可以下一個random(singleRange, singleRange * -1)
"""

timeIndex = pd.date_range(startTime, periods = 270, freq="min")

predict = pd.DataFrame(np.random.randn(len(timeIndex)), columns=["twStock"], index = timeIndex)
