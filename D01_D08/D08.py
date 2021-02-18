import numpy as np
import os
if os.name=='name':
    os.system('cls')
else:
    os.system('clear')


name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]
dt = np.dtype({'names':('Name', 'Sex', 'Weight', 'Rank','Myopia'), 'formats':('U5', 'U5', 'f8', 'U3','?')})

#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
c=np.zeros(8,dtype=dt)
c['Name']=name_list
c['Sex']=sex_list
c['Weight']=weight_list
c['Rank']=rank_list
c['Myopia']=myopia_list

#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重
avg_weight=np.mean(c['Weight'])
print('Average of weight=',avg_weight)

#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重
avg_boy_weight=np.mean(c[c['Sex']=='boy']['Weight'])
print('Average of weight within boys=',avg_boy_weight)

#3. 呈上題，進一步算出女生(sex欄位是girl)平均體重
avg_boy_weight=np.mean(c[c['Sex']=='girl']['Weight'])
print('Average of weight within girls=',avg_boy_weight)