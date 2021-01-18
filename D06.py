import os
import numpy as np
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')


array1=np.array(range(30))
array2=np.array([2,3,5])

with open ('multi_array.npz','wb') as f:
    np.savez(f,array1=array1,array2=array2)
npz=np.load('multi_array.npz')


with open('multi_array_2.npz','wb') as f:
    np.savez(f,array1=npz[npz.files[0]],array2=npz[npz.files[1]])
