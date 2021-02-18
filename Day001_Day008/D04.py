import numpy as np
import os
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

#1
larger=np.greater(english_score,math_score)
n=0
sum_larger=sum([n+1 for i in larger if i])
print(sum_larger)#<-------Anser

#2
TrueOrNot=True
for i in range(len(chinese_score)):
    if chinese_score[i]< english_score[i] and chinese_score[i]<math_score[i]:
        TrueOrNot=False
        break
print(TrueOrNot)#<--------Anser