#!/usr/bin/env python
# coding: utf-8

# 作業目標:<br>
# 1. 敘述統計量計算<br>
# 2. 運用自定義函數apply

# 作業重點:<br>
# 1. 了解敘述統計量並解釋<br>
# 2. 運用apply時須注意自定義函數寫法

# 題目<br>
# 對以下成績資料做分析<br>
# 1. 6號學生(student_id=6)3科平均分數為何?<br>
# 2. 6號學生3科平均分數是否有贏過班上一半的同學?<br>
# 3. 由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問6號同學3科成績分別是?<br>
# 4. 承上題，加分後各科班平均變多少?
# <br>
# score_df = pd.DataFrame([[1,56,66,70], 
#               [2,90,45,34],
#               [3,45,32,55],
#               [4,70,77,89],
#               [5,56,80,70],
#               [6,60,54,55],
#               [7,45,70,79],
#               [8,34,77,76],
#               [9,25,87,60],
#               [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])

# In[2]:


import pandas as pd
score_df = pd.DataFrame([[1,56,66,70], 
              [2,90,45,34],
              [3,45,32,55],
              [4,70,77,89],
              [5,56,80,70],
              [6,60,54,55],
              [7,45,70,79],
              [8,34,77,76],
              [9,25,87,60],
              [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
score_df = score_df.set_index('student_id')
score_df


# In[13]:


#1.6號學生(student_id=6)3科平均分數為何?
student6_mean_score=score_df.loc[6,['math_score','english_score','chinese_score']].mean()
print(student6_mean_score)


# In[14]:


#2. 6號學生3科平均分數是否有贏過班上一半的同學
class_mean=score_df.mean(axis=1)
class_mean_mean=class_mean.mean()
if student6_mean_score>class_mean_mean:
    print(True)
else:
    print(False)


# In[23]:


#由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問6號同學3科成績分別是?
shift_class_df=score_df.apply(lambda x:(x**0.5)*10)
shift_student6=shift_class_df.loc[6]
print(shift_student6)


# In[16]:


#承上題，加分後各科班平均變多少


# In[24]:


shift_class_mean=shift_class_df.mean(axis=1)
print(shift_class_mean)


# In[ ]:




