import time
import random
import sys

class Oyuncu:
    def __init__(self,adi,can=5,enerji=100):
        self.isim=adi
        # self.cani=can
        self.enerjisi=enerji
        self.saldirigucu=random.randint(0,50)
        self.darbe=0

    def oyuncuGoster(self):
        print( "{} isimli oyuncu özellikleri:\n" \
               "Enerjisi: {}\n" \
               "Saldiri gücü: {}\n".format(self.isim,self.enerjisi,self.saldirigucu))
    def saldir(self,rakip):
        print("saldiriliyor.")
        for i in range(5):
            # time.sleep(0.3)
            print("#",sep="",flush=True)
        self.darbeVur(rakip)

    def darbeVur(self,rakip):
        self.sonuc=random.randint(0,2)
        if self.sonuc==0:
            print("ISKA\n!!")
        elif self.sonuc==1:
            rakip.enerjisi-=random.randint(0,10)
            print("rakibe saldırıldı\n",rakip.enerjisi)
        elif self.sonuc==2:
            self.enerjisi-=random.randint(0,10)
            print("rakip karşılık verdi:\n",self.enerjisi)

    # def kontrolEt(self):
    #     if self.enerjisi<50:
    #         print("Oyuncunun canı azaldı, canı {}".format(self.enerjisi))
    #     elif


o1=Oyuncu("Mehmet")
o2=Oyuncu("Kemal")
while True:
    print("Saldırı için s\n"
          "çıkmak için ç")
    secim=input("Seçiminiz: \n")
    if secim=="s":
        o1.saldir(o2)
    elif secim=="ç":
        sys.exit()


#
# o2.oyuncuGoster()
#
# o2.saldir(o1)









