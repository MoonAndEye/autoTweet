
import matplotlib.pyplot as plt


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
d_highest = 100000
d_lowest = 8000

timeIndex = periodTime([9,0], [13,30], 10)

fig, ax = plt.subplots()

plt.axis([timeIndex[0], timeIndex[-1], d_lowest - 200, d_highest + 200])

new = []
for a in range(0,len(timeIndex)-1):
    if a%3 == 0:
        new.append(timeIndex[a])

ax.set_xticks(new, minor=False)
#ax.set_xticks([0.3,0.55,0.7], minor=True)
ax.xaxis.grid(True, which='major')
ax.xaxis.grid(True, which='minor')
plt.show()
