import numpy
import pandas as pd
import os

if os.name=='name':
    os.system('cls')
else:
    os.system('clear')

#1
filename='boston.csv'
df1=pd.read_csv(filepath_or_buffer='boston.csv',sep=',')
target=['CHAS','NOX','RM']
df1[target].to_excel('output.xlsx',sheet_name='sheet_name_1',engine='openpyxl')