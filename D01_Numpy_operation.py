import numpy as np
import os
os.system('clear')


#1
array_1=np.arange(0,20+1)
print(array_1)
#2
where=np.where(array_1%2==0)
array_2=array_1[where]
print(array_2)
#2
where=np.where(array_1%3==0)
array_3=array_1[where]
print(array_3)