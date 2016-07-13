# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:08:04 2016

"""
import pandas as pd
import time
import datetime
import matplotlib as plt
import random as rd

time_axis = []

"""
三個小時半的交易, 就是270 min
"""


startTime = "09:01"
test = pd.date_range(startTime, periods = 270, freq="min")

"""
for each_m in range(210):
    time = startTime + each_m
    time_axis.append(time)
"""
