import random
k_secim=input("seçiminiz[t,ç,b] :")
secim=["t","ç","b"]


def topla():
    a=int(input("birinci sayıyı giriniz :"))
    b = int(input("ikinci sayıyı giriniz :"))

    return print(a+b)

def cikar():
    a = int(input("birinci sayıyı giriniz :"))
    b = int(input("ikinci sayıyı giriniz :"))
    if a>b: return print(a-b)
    else: return print(b-a)

def bol():
    a = int(input("birinci sayıyı giriniz :"))
    b = int(input("ikinci sayıyı giriniz :"))
    if a > b: return print(a//b)
    else: return print(b//a)
#
islemler ={"t":topla,"ç":cikar,"b":bol}
if k_secim=="t": islemler["t"]()
elif k_secim=="ç": islemler["ç"]()
elif k_secim=="b": islemler["b"]()


#
#
#

