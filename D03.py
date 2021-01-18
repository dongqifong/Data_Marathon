import numpy as np
import os
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')

#1
V1=20000
V0=20
db=20*np.log10(V1/V0)#<---------anser
print(db)

#2
#db=20log10(V/V0)
#V=10^(db/20)*V0
#V2/V1=10^((db2/20-db1/20)*V0)
db1=30
db2=50
ratio=np.power(10,(db2-db1)/10)#<--------anser
print(ratio)