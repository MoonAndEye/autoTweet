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
    
timeAMIndex = periodTime([9,0], [11,30], 10)

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
nikkeiJson = getQuotes('INDEXNIKKEI:NI225')

b4 = []

for each in nikkeiJson[0]:
    b4.append(each)

result = nikkeiJson[0][b4[5]]
startPoint = float(result[-9:].replace(",",""))


singleRange = startPoint * 0.05
singleRange = int(singleRange)
up_limit = rd.randint(int(startPoint),int(startPoint + singleRange))
low_limit = rd.randint(int(startPoint - singleRange), int(startPoint))

"""
singleRange 是單邊範圍,到時候可以下一個random(singleRange, singleRange * -1)
"""

"""
timeAMIndex = pd.date_range(startTime, periods = 27, freq="10min",)
datelist = pd.date_range(startTime, periods = 27, freq="10min",).tolist()
"""

#改成每十分鐘一點,畫面比較漂亮,如果想的話,每1分鐘一點也行
#print(len(timeAMIndex))

minutes_point = []

for each_min in range(len(timeAMIndex)):
    each_point = rd.randint(low_limit, up_limit)
    minutes_point.append(each_point)

predict = pd.DataFrame(minutes_point, columns=["jpStock"], index = timeAMIndex)

timeRestIndex = periodTime([11,00], [12,20], 10)
timeRestIndex = timeRestIndex[4:]

restPredict = pd.DataFrame(columns=["jpStock"], index = timeRestIndex)
restPredict = restPredict.fillna(predict.jpStock[-1])

timePMIndex = periodTime([12,00], [15,00], 10)
timePMIndex = timePMIndex[3:]

minutes_point_pm = []

for each_min in range(len(timePMIndex)):
    each_point = rd.randint(low_limit, up_limit)
    minutes_point_pm.append(each_point)

predict_pm = pd.DataFrame(minutes_point_pm, columns=["jpStock"], index = timePMIndex)

frames = [predict, restPredict, predict_pm]

predict = pd.concat(frames)


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
start = predict.jpStock[0]
d_highest = predict.jpStock.max()
d_lowest = predict.jpStock.min()
final = predict.jpStock[-1]

"""
#以下是舊版本的,可是格線出問題,不在我想要的位置上
plt.plot(timeIndex, minutes_point)

plt.gcf().subplots_adjust(bottom=0.2)
plt.axis([timeIndex[0], timeIndex[-1], d_lowest - 200, d_highest + 200])
plt.xlabel('Time')
plt.ylabel('nikkei')
plt.title('Taiwan stock index Predict on ' + title)
#plt.axis([0, 6, 0, 20])
plt.xticks(rotation=30)
plt.grid(True)

plt.show()
fileName = "nikkei.jpg"


#如果要把 figure 存起來, 就要把 plt.show() 關掉
#plt.savefig(fileName)   # save the figure to file
plt.close()
"""

newX = predict.index.values
fig, ax = plt.subplots()

plt.axis([newX[0], newX[-1], d_lowest - 200, d_highest + 200])
plt.xlabel('Time')
plt.ylabel('nikkei')
plt.title('Nikkei stock index Predict on ' + title)
#plt.axis([0, 6, 0, 20])
plt.xticks(rotation=30)


newAxis = []
for a in range(0,len(newX)-1):
    if a%3 == 0:
        newAxis.append(newX[a])
newAxis.append(newX[-1])
"""
#newAxis是我想要放上去的軸,因為newAxis 從 timeIndex來, 兩者有對應關係
"""
ax.set_xticks(newAxis, minor=False)
#ax.set_xticks([0.3,0.55,0.7], minor=True)
ax.xaxis.grid(True, which='major')
ax.xaxis.grid(True, which='minor')
plt.grid(True)

newY = []

for each in predict["jpStock"]:
    newY.append(each)

plt.plot(newX, newY)
#plt.show()
plt.xticks(rotation=30)


predict.rename(columns={'jpStock':fileName}, inplace=True)

savepath = fileName + "_jp.csv"
#plt.show()
plt.savefig(fileName + "_jp.jpg")
plt.close()
predict.to_csv(savepath)

print("Open:"+ str(start))
print("Max:"+ str(d_highest))
print("Min:"+ str(d_lowest))
print("Close:"+ str(final))
print("This graph was made by random module.")
print("")
print("#Nikkei random prediction")
print("#No response for the graph")
print("#The graph was made by Python")
