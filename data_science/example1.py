import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool


my_data=pd.read_csv('poke_data/pokemon.csv')

# print(my_data.info())


# print(my_data.head(7))
newdata=my_data.drop(columns='#')
# print(newdata.head(7))

# print(newdata.columns)
# for i in newdata.columns:
#     # newdata.columns=newdata.columns.append(i.lower())
#     print(i.lower())
#     newdata.columns=i.lower()
newdata.columns=[i.replace('.','')  for i in newdata.columns]

newdata.columns=[i.lower() for i in newdata.columns]

newdata.columns=[i.replace(' ','_') for i in newdata.columns]

# print(newdata.columns)

print(newdata.head())

corr_table=newdata.loc[:5,'hp':'speed']



print(corr_table.corr())

plt.subplot(figsize=(18,18))
plt.legend()
f,ax=plt.subplots()
ax.plot()
# print(newdata.corr())

# print(newdata.rank())

sns.heatmap(corr_table,cmap='**',linewidths=1)

'''data, vmin, vmax, cmap, center, robust, annot, fmt, annot_kws, 
linewidths, linecolor, cbar, cbar_kws, cbar_ax, square, xticklabels, yticklabels, mask,
,vmax=1





'''