

import pandas as pd
import numpy as np
import xlrd


df=pd.read_excel("data.xlsx")

print(df.head())






























# columns=['TÜKETİCİ FİYATLARI ENDEKSİ (TÜFE)', 'Unnamed: 1', 'Unnamed: 2',
#        'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7',
#        'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12',
#        'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16',
#        'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20',
#        'Unnamed: 21', 'Unnamed 22']
# #
# year = 2008
# for inx , val in enumerate(columns):
#     if inx == 0:
#         columns[inx]="months"
#
#     elif inx % 2 == 1:
#         columns[inx]= str(year)+"_year"
#
#
#     else:
#         columns[inx]= str(year)+"_year"
#         year += 1
#
# list=[]**5
#
#
# list[1]="guur"
# list[2]=2
#
# print(list)





# for inx,val in enumerate(columns):
#
#     print(inx,"   ",val)

# for i in columns:
#     print("index", columns.index(i))
