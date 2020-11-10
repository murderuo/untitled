class Calisan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()
    @classmethod
    def personel_sayısını_görüntüle(cls):
        if len(cls.personel)==0:
            print("Personel Yok")
        else:
            print("Personel Sayısı: ",len(cls.personel))
    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))
    @classmethod
    def personeli_görüntüle(cls):
        if len(cls.personel)==0:
            print("Personel Yok")
        else:
            print('Personel listesi:')
            for kişi in cls.personel:
                print(kişi,sep="")
    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

c1=Calisan("Ahmet")
c2=Calisan("mehmet")
print(dir(Calisan))
print(dir(c1))

#

# # c3=Calisan("Aysel")
#
#
# Calisan.personeli_görüntüle()
#
# Calisan.personel_sayısını_görüntüle()