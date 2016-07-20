from googlefinance import getQuotes

import json

test = json.dumps(getQuotes('TPE:TAIEX'))

a = getQuotes('TPE:TAIEX')

empty = []

for each in a[0]:
    empty.append(each)

#a = []

result = a[0][empty[5]]
new = float(result.replace(",",""))

new = int(new)
print(result)
print(type(result))
print((float(result.replace(",",""))))
