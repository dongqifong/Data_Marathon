import numpy as np
import os
if os.name=='name':
    os.system('cls')
else:
    os.system('clear')

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])


def information(targetlist):
    Avg=np.nanmean(targetlist)
    Max=np.nanmax(targetlist)
    Min=np.nanmin(targetlist)
    Std=np.nanstd(targetlist)
    return Avg,Max,Min,Std

#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
##English

avg_eng,max_eng,min_eng,std_eng=information(english_score)
print('---------------Statistics of English----------------')
print('Average of English:',avg_eng)
print('Maximum of English:',max_eng)
print('Minimum of English:',min_eng)
print('Std of English:',std_eng)
print()

avg_math,max_math,min_math,std_math=information(math_score)
print('---------------Statistics of Math----------------')
print('Average of Math:',avg_math)
print('Maximum of Math:',max_math)
print('Minimum of Math:',min_math)
print('Std of Math:',std_math)
print()

avg_chinese,max_chinese,min_chinese,std_chinese=information(chinese_score)
print('---------------Statistics of Chinese----------------')
print('Average of chinese:',avg_chinese)
print('Maximum of chinese:',max_chinese)
print('Minimum of chinese:',min_chinese)
print('Std of chinese:',std_chinese)
print()

#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[4]=55
avg_math,max_math,min_math,std_math=information(math_score)
print('---------------Statistics of Math----------------')
print('Average of Math:',avg_math)
print('Maximum of Math:',max_math)
print('Minimum of Math:',min_math)
print('Std of Math:',std_math)
print()

#3. 用補考後資料找出與國文成績相關係數最高的學科?
matrix=np.array([english_score.T,math_score.T,chinese_score.T])
if matrix[0][2]>matrix[1][2]:
    print('The subject that has maximum correlation coefficient with Chinese: English')
else:
    print('The subject that has maximum correlation coefficient with Chinese: Math')
