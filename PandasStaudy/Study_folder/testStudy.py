from matplotlib.finance import quotes_historical_yahoo_ohlc
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotesMS = quotes_historical_yahoo_ohlc('MSFT', start, today)
attributes = ['date', 'open', 'close', 'high', 'low', 'volume']
quotesDFMS = pd.DataFrame(quotesMS, columns = attributes)
list = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesDFMS.index = list
quotesDFMS = quotesDFMS.drop(['date'], axis = 1)
list = []
quotesDFMS14 = quotesDFMS['14/01/01':'14/12/31']
#===============================================================================
# print quotesDFMS14.index[0][3:5]
#===============================================================================
for i in range(0, len(quotesDFMS14)):
    list.append(int(quotesDFMS14.index[i][3:5]))
##quotesDFMS14['month'] = list
print quotesDFMS['14/01/30':'14/10/30'].sort('volume')

#===============================================================================
# print quotesDFMS14.groupby('month').mean().close
#===============================================================================
