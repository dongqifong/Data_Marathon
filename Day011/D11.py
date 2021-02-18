#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
os.system('clear')
q_df = pd.DataFrame([['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],columns=['Sex','Profession'])


# In[49]:


#缺失值填入字串'others'


# In[50]:


q_df=q_df.fillna("others")


# In[51]:


print(q_df)


# In[52]:


#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?
#因為性別和職業是沒有順序性的
#所以用one-hot encoding


# In[53]:


sex=pd.get_dummies(q_df["Sex"])
profession=pd.get_dummies(q_df["Profession"])
q_df=pd.concat([q_df,sex],axis=1)
q_df=pd.concat([q_df,profession],axis=1)


# In[54]:


print(q_df)


# In[ ]:




