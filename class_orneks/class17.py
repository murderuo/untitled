class Oyuncu():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0
    def hareket_et(self):
        print('hareket ediliyor...')
    def puan_kazan(self):
        print('puan kazanıldı')
    def puan_kaybet(self):
        print('puan kaybedildi')

class Asker(Oyuncu):
    pass

class İsci(Oyuncu):
    pass

class Yonetici(Oyuncu):
    pass


asker1=Asker("Ahmet","Er")

print(asker1.isim,asker1.rütbe,asker1.güç)

asker1.puan_kazan()