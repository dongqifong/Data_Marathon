#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import os


# In[6]:


#1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
#2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?


# In[17]:


filename="boston.csv"
df=pd.read_csv(filename)
df.boxplot()
print('Tax的中位數在300~400間')
print(df[df.median<400])


# In[16]:


#關係為負相關
#意即NOX變大則DIS大略都是變小
df.plot.scatter(x="NOX",y="DIS")


# In[ ]:




