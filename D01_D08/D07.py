import numpy as np
import os
if os.name=='name':
    os.system('cls')
else:
    os.system('clear')

#1
print('#1')
array1=np.array([[10,8],[3,5]])
array1_inv=np.linalg.inv(array1)

dot_result=np.rint(np.dot(array1,array1_inv))
I2=np.identity(2,dtype=int)


if np.array_equal(dot_result,I2):
    print(True)
else:
    print(False)

#2
print()
print('#2')
w,v=np.linalg.eig(array1)
print('eigenvalue=',w)
print('eigenvector=',v)

#3
print()
print('#3')
u,s,vh=np.linalg.svd(array1)
print('u=',u)
print('s=',s)
print('vh=',vh)