# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:08:04 2016
"""
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import random as rd
from googlefinance import getQuotes
import json

def periodTime(start=list, end=list, step=int):
    """
    You must import datetime
    Start and end is a list with two elements.
    Ex. you can use [9,0] as 09:00, [13,30] as 13:00
    """ 
    output= []
    for hours in range(start[0], end[0] + 1):
        if hours < end[0]:
            for minutes in range(0,60, 10):
                temp = datetime.time(hours,minutes)
                output.append(temp)
        if hours == end[0]:
            for minutes in range(start[1], end[1] + 1, step):
                temp = datetime.time(hours, minutes)
                output.append(temp)
    
    return (output)
    
timeIndex = periodTime([9,0], [13,30], 10)

time_axis = []

today = datetime.datetime.today()
#tmr = today
tmr = today + datetime.timedelta(1)
title= tmr.strftime("%Y %B %d %A .")

fileName = (tmr.strftime("%Y") + "-"+ tmr.strftime("%m") + "-"+ tmr.strftime("%d"))

print(str(tmr.strftime("%Y %B %d %A .")))


"""
日股上午 0900 - 1130
日股下午 1230 - 1500
"""


#startTime = "09:00"
#startPoint = 9007.68
"""
把start 改成自動取得
"""
taiexJson = getQuotes('TPE:TAIEX')

b4 = []

for each in taiexJson[0]:
    b4.append(each)

result = taiexJson[0][b4[5]]
startPoint = float(result[-8:].replace(",",""))
#startPoint = 9013.14

singleRange = startPoint * 0.05
singleRange = int(singleRange)
up_limit = rd.randint(int(startPoint),int(startPoint + singleRange))
low_limit = rd.randint(int(startPoint - singleRange), int(startPoint))

"""
singleRange 是單邊範圍,到時候可以下一個random(singleRange, singleRange * -1)
"""

"""
timeIndex = pd.date_range(startTime, periods = 27, freq="10min",)
datelist = pd.date_range(startTime, periods = 27, freq="10min",).tolist()
"""

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
toDO List
a >要把檔名改用日期,不過日期不是字串的話不能合併,之後修
b >圖的最左邊,要設09:00右邊要設13:30,現在的軸也不對,而且1330的資料沒有
c >判斷式也沒寫,如果是假日,台股不開盤,所以就不用執行程式了
d >還要把 始 高 低 終 的值print出來,這之後也要貼在 twitter上
"""
start = predict.twStock[0]
d_highest = predict.twStock.max()
d_lowest = predict.twStock.min()
final = predict.twStock[-1]

"""
#以下是舊版本的,可是格線出問題,不在我想要的位置上
plt.plot(timeIndex, minutes_point)

plt.gcf().subplots_adjust(bottom=0.2)
plt.axis([timeIndex[0], timeIndex[-1], d_lowest - 200, d_highest + 200])
plt.xlabel('Time')
plt.ylabel('TAIEX')
plt.title('Taiwan stock index Predict on ' + title)
#plt.axis([0, 6, 0, 20])
plt.xticks(rotation=30)
plt.grid(True)

plt.show()
fileName = "TAIEX.jpg"


#如果要把 figure 存起來, 就要把 plt.show() 關掉
#plt.savefig(fileName)   # save the figure to file
plt.close()
"""
fig, ax = plt.subplots()

plt.axis([timeIndex[0], timeIndex[-1], d_lowest - 200, d_highest + 200])
plt.xlabel('Time')
plt.ylabel('TAIEX')
plt.title('Taiwan stock index Predict on ' + title)
#plt.axis([0, 6, 0, 20])
plt.xticks(rotation=30)


newAxis = []
for a in range(0,len(timeIndex)-1):
    if a%3 == 0:
        newAxis.append(timeIndex[a])
newAxis.append(timeIndex[-1])
"""
#newAxis是我想要放上去的軸,因為newAxis 從 timeIndex來, 兩者有對應關係
"""
ax.set_xticks(newAxis, minor=False)
#ax.set_xticks([0.3,0.55,0.7], minor=True)
ax.xaxis.grid(True, which='major')
ax.xaxis.grid(True, which='minor')
plt.grid(True)
plt.plot(timeIndex, minutes_point)
#plt.show()
plt.xticks(rotation=30)


predict.rename(columns={'twStock':fileName}, inplace=True)

savepath = fileName + "_tw.csv"
plt.savefig(fileName + "_tw.jpg")
plt.close()
predict.to_csv(savepath)

print("開盤:"+ str(start))
print("最高:"+ str(d_highest))
print("最低:"+ str(d_lowest))
print("收盤:"+ str(final))
print("以上是用python的random模組隨機跑，完全不準。")
print("盈虧自負")
print("#台股隨機預測")
print("#不負責任預測")
print("#用python來畫圖")
