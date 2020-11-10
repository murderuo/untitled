import time

def zaman_hesapla(fonksiyon):
    def wrapper(sayılar):
        baslama=time.time()
        sonuç=fonksiyon(sayılar)
        bitis=time.time()
        print(fonksiyon.__name__+" "+str(bitis-baslama)+" saniye sürdü.")
        return sonuç
    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuç=[]
    for i in sayılar:
        sonuç.append(i ** 2)
    return sonuç

@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuç=[]
    for i in sayılar:
        sonuç.append(i ** 3)
    return sonuç

print(kareleri_hesapla(range(100000)))

print(küpleri_hesapla(range(100000)))