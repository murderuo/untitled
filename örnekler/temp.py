import numpy as np

dt={'% Pro/Sup':[1,2,3,4],
    '% Pro/Sale':[10,20,30,40],
    '% Pro/Exc.Fee':[100,200,300,400]}

def rate(df):
    subjects=['% Pro/Sup','% Pro/Sale','% Pro/Exc.Fee']
    outputdic=dict()
    for i in subjects:
        edges=['np.min','np.max','np.mean','np.std']
        for j in range(len(edges)):  #
            nameof=edges[j]+i  #
            v=list(map(lambda x:eval(x)(df[i]),edges))
            outputdic[nameof]=v[j]  #
    for item,value in outputdic.items():
        print(item,value)
    # return outputdic

rate(dt)