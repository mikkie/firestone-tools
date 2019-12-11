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
       if(index in ["002149", "600459", "600988", "000758", "002716", "002167", "600115", "600548", "601111", "601021", "600029", "600004", "601518", "603885", "000828", "002627", "000089", "600377", "600350", "601006", "600033", "600221", "601333", "002357", "600561", "300178", "002682", "600020", "600009", "600012", "000796", "002815", "002913", "603386", "603933", "300346", "002510", "300707", "600611", "002838", "002501", "002160", "002540", "300217", "603305", "300248", "000606", "300663", "300300", "300469", "300532", "002649", "300634", "300377", "300085", "002316", "300020"]):
         res.append(index)
print(','.join(res))
print(len(res))

