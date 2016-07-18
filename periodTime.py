# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:08:04 2016

"""
import pandas as pd
import numpy as np
#import time
import datetime
import matplotlib as plt
import random as rd


d0 = datetime.date.today()
start = datetime.datetime.today()
start = start.replace(hour=9,minute=0)
start = start + datetime.timedelta(minutes = 30)
#print(start)
d0 = d0 - datetime.timedelta(minutes = 10)   #如果以後要換日期，就用這個
#test = [start]
a = datetime.time(9,0)
b = datetime.time(13,10)

print(a,b)

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
    
test = periodTime([9,0], [13,30], 10)
#print(test)

for each in test:
    print(each)
