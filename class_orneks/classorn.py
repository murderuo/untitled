import random

class Sinif():
    def __init__(self):
        print("Nesne oluşturuldu")
        pass

    def ad(self,adi,soyadi):
        self.adi=adi
        self.soyadi=soyadi

    def adgoster(self):
        return self.adi,self.soyadi

    def degerata(self):
        self.deger=random.randint(1,100)

    def degergoster(self):
        print(self.deger)
        return self.deger

    def degerarttir(self):
        self.deger=self.deger+random.randint(1,999)
        print(self.deger)
        return self.deger
    @classmethod
    

    @staticmethod
    def tel_no(telefon):
        tel=telefon.split(" ")
        return tel



personel=Sinif()

personel.ad("uğur","okur")

y_tel=personel.tel_no("0537 544 79 79")

print(y_tel)


# pbilgi=nesne1.adgoster()
#
# print(pbilgi)





#
# nesne1=Sinif()
#
# # nesne2=Sinif()
#
# nesne1.ad("birinci nesne","ikinci nesne")
#
# # ad,soyad=nesne1.adgoster()
#
# nesne1.degerata()
#
# n1_degeri=nesne1.degergoster()
#
# nesne1.degerarttir()
#
# n1_yeni_degeri=nesne1.degergoster()
#
# # fark=nesne1.degerarttir()
# # print("fark: ", fark)
#
# print(n1_degeri)
# print(n1_yeni_degeri)
#
# # print(ad,soyad)
#


