import jqdata
import numpy as np
import talib as ta
from datetime import datetime

res = []
executeDate = datetime.now()
executeDateStr = '{}-{}-{}'.format(executeDate.year, ('0' + str(executeDate.month))[-2:], ('0' + str(executeDate.day))[-2:])
df_all = get_all_securities(types=['stock'], date=executeDateStr)
for index,row in df_all.iterrows():
    df_stock = get_price(index, end_date=executeDateStr, frequency='daily', fields=['close','high','low'], skip_paused=True, fq='pre', count=120)
    high_row = df_stock.loc[df_stock['high'].idxmax()]
    high = high_row.get('high')
    low_row = df_stock.loc[df_stock['low'].idxmin()]
    low = low_row.get('low')
    lastClose = df_stock.iloc[-1].get('close')
    flag = False
    if (lastClose - low) / (high - low) < 0.1:
      df_temp = df_stock[-5:]
      high_row = df_temp.loc[df_temp['high'].idxmax()]
      high = high_row.get('high')
      low_row = df_temp.loc[df_temp['low'].idxmin()]
      low = low_row.get('low')
      if (lastClose - low) / low < 0.03:
         flag = True 
    if flag:
       index = index.replace('.XSHE','').replace('.XSHG','') 
       if(index in ${codes}):
         res.append(index)
print(','.join(res))
print(len(res))

