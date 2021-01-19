import numpy as np
import pandas as pd
import os
if os.name=='name':
    os.system('cls')
else:
    os.system('clear')
#讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv
filename1='STOCK_DAY_0050_202009.csv'
filename2='STOCK_DAY_0050_202009.csv'
df1=pd.read_csv(filename1)
df2=pd.read_csv(filename2)
#串聯+找出open小於close的資料
df3=pd.concat([df1[df1['open']<df1['close']],df2[df2['open']<df2['close']]],axis=1)

print(df3)