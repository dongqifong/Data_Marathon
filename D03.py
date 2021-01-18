import numpy as np
import os
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')

#1
V1=20000
V0=20
db=10*np.log10(V1)/np.log(V0)#<---------anser
print(db)

#2
#db=10log10(V)
#V=10^(db/10)
#V2/V1=10^(db2/10-db1/10)
ratio=np.power(10,(db2-db1)/10)#<--------anser
print(ratio)