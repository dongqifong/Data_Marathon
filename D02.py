import numpy as np
import os
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
#1
array1=np.array(range(30))
array1=array1.reshape((5,6),order='F')
print(array1)
#2
where=np.where((array1-1)%6==0)
print(where)