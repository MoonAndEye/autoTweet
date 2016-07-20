from googlefinance import getQuotes

import json

print (json.dumps(getQuotes('TPE:TAIEX'), indent=2))
