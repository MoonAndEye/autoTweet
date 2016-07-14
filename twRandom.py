# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:08:04 2016

"""
import pandas as pd
import numpy as np
import time
import datetime
import matplotlib.pyplot as plt
import random as rd

time_axis = []

"""
四個小時半的交易, 就是270 min
"""


startTime = "09:01"
startPoint = 8832.42
singleRange = startPoint * 0.1
singleRange = int(singleRange)
up_limit = rd.randint(int(startPoint),int(startPoint + singleRange))
low_limit = rd.randint(int(startPoint - singleRange), int(startPoint))

"""
singleRange 是單邊範圍,到時候可以下一個random(singleRange, singleRange * -1)
"""

timeIndex = pd.date_range(startTime, periods = 27, freq="10min",)
prettyIndex =[]

#改成每十分鐘一點,畫面比較漂亮,如果想的話,每1分鐘一點也行
#print(len(timeIndex))

minutes_point = []

for each_min in range(len(timeIndex)):
    each_point = rd.randint(low_limit, up_limit)
    minutes_point.append(each_point)

predict = pd.DataFrame(minutes_point, columns=["twStock"], index = timeIndex)

"""
for each_min in range(len(timeIndex) -1):
    init = min_index[each_min]
    nextPoint = init + rd.randint(int(-singleRange), singleRange)
    min_index.append(nextPoint)    
"""
"""
一開始丟出一個上限,和一個下限

然後 random 的東西就直接設定在這區間,就不會超過啦

先畫圖,之後再改點數,這個點數很不正常,可能要加入一常態分佈的狀況
目前先設定上下限, 當天的上下限就只會在這個地方跑

toDo List
1> 做出三種 pattern
    a> 開高走高
    b> 開低走低
    c> 上下震盪

"""

"""

"""


plt.plot(timeIndex, minutes_point)
plt.xlabel('Time')
plt.ylabel('TAIEX')
plt.title('Taiwan stock index Predict')
#plt.axis([0, 6, 0, 20])
plt.xticks(rotation=70)

plt.show()
fileName = "TAIEX.jpg"

"""
#如果要把 figure 存起來, 就要把 plt.show() 關掉
#plt.savefig(fileName)   # save the figure to file
#plt.close()
"""
