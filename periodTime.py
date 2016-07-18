import datetime


def periodTime(start=list, end=list, step=int):
    """
    You must import datetime
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
