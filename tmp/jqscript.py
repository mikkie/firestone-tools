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
       if(res in ["600860", "002783", "002272", "603637", "600803", "603776", "000669", "002488", "000723", "300179", "300376", "600875", "600273", "300145", "000698", "603938", "300540", "601678", "600746", "002054", "000551", "002002", "002012", "002140", "002469", "002498", "600458", "600141", "600248", "603698", "600470", "001896", "603113", "601777", "000980", "600379", "600759", "300435", "002564", "600691", "002274", "000755", "002249", "002408", "002628", "603045", "600758", "600727", "300471", "002648", "002733", "002639", "002665", "300234", "000637", "600846", "002549", "600997", "300072", "002709", "300228", "002221", "300091", "300375", "002080", "601965", "300325"]):
         res.append(index)
print(','.join(res))
print(len(res))

