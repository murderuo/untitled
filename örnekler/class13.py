import random
import sys

class Oyuncu:
    def __init__(self,ad):
        self.adi=ad
        self.saldiri_gucu=random.randint(1,13)
        self.enerji=random.randint(50,100)

    def oyuncu_bilgisi(self):
        print("Oyuncu adi:{}\n"
              "Saldiri gucu:{}\n"
              "Enerjisi: {}".format(self.adi,self.saldiri_gucu,self.enerji))

    def atak_degeri(self):
        self.deger = random.randint(0, 2)
        return self.deger

    def saldiriyap(self,rakip):
        self.secenek=self.atak_degeri()
        if self.secenek==0:
            print("ISKA !!")
        elif self.secenek==1:
            self.darbe(rakip)
            print("Rakip durumu:\n")
            rakip.oyuncu_bilgisi()
        elif self.secenek==2:
            self.darbe(self)
            print("Oyuncu durumu:\n")
            self.oyuncu_bilgisi()
        # if rakip.durum<25:
        #     print("rakip ölmek üzere")

    def darbe(self,rakip):
        rakip.enerji-=self.saldiri_gucu
        if rakip.enerji<25:
            print("rakip ölmek üzere..")




ahmet=Oyuncu("ahmet")

mehmet=Oyuncu("mehmet")


while True:
    ahmet.oyuncu_bilgisi()
    mehmet.oyuncu_bilgisi()

    print("saldırı için s\n"
          "çıkmak için q\n"
          "seçiminiz:\n")
    secim=input(">>>")
    if secim=="s":
        ahmet.saldiriyap(mehmet)

    elif secim=="q":
        sys.exit()



