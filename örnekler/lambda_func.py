'''tanımlanan fonksiyonu tek satırda kısaca oluşturmamızı sağlar'''

#basir bir fonksiyon şöyle olur

import pandas as pd
def topla(x,y):

    return x+y

print(topla(5,9))


#lambda function ise şu şekilde oluşturulabilir


#foksiyon adı   #x değişkeni,#y değişkeni : #return edilecek değer
top =lambda x,y: x+y

print(top(3,4))

squarre = lambda x: x**2

print(squarre(5))

yazdir= lambda : print("sadece yazdirma islevi")

yazdir()


liste=["Ankara","İZMİR","İSTANBUL"]
df=pd.DataFrame(liste)
print(df)

df=df.apply(lambda x: str(x).lower() )

print(df)





