sesli_harfler="aeıioöuü"

sayac=0

def kelime_sor():
    kel=input("kelimeyi giriniz :")
    return kel

def seslidir(h):
    return h in sesli_harfler

def arttir(sayac,kelime):
    for harf in kelime:
        if seslidir(harf):
            sayac+=1
    return sayac

def ekrana_bas (kelime):
    mesaj="{} kelimesinde {} tane sesli harf vardır".format(kelime,arttir(sayac,kelime))
    print(mesaj)

def calistir():
    kelime=kelime_sor()
    ekrana_bas(kelime)

calistir()



