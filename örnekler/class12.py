import time
import random
import sys

class Oyuncu:

    def __init__(self, isim, can=5, enerji=100):
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji

    def mevcut_durumu_görüntüle(self):
        print('darbe: ', self.darbe)
        print('can: ', self.can)
        print('enerji: ', self.enerji)

    def saldir(self, rakip):
        print('Bir saldirı gerçekleştirdiniz.')
        print('saldirı sürüyor. Bekleyiniz.')
        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
        sonuc = self.saldirı_sonucunu_hesapla()
        if sonuc == 0:
            print('\nsonuc: kazanan taraf yok')
        elif sonuc == 1:
            print('\nsonuc: rakibinizi darbelediniz')
            self.darbele(rakip)
        elif sonuc == 2:
            print('\nsonuc: rakibinizden darbe aldınız')
            self.darbele(self)

    def saldirı_sonucunu_hesapla(self):
        return random.randint(0, 2)

    def kaç(self):
        print('Kaçılıyor...')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)
            print('Rakibiniz sizi yakaladı')

    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= random.randint(0,10)
        if (darbelenen.darbe % 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print('Oyunu {} kazandı!'.format(self.isim))
            self.oyundan_çık()
    def oyundan_çık(self):
        print('Çıkılıyor...')
        sys.exit()
##################################
# Oyuncular
siz = Oyuncu('Ahmet')
rakip = Oyuncu('Mehmet')

# siz.darbele(rakip)
print(siz.saldirı_sonucunu_hesapla())
siz.mevcut_durumu_görüntüle()
rakip.mevcut_durumu_görüntüle()
# Oyun başlangıcı
while True:
    print('Şu anda rakibinizle karşı karşıyasınız.',
    'Yapmak istediğiniz hamle: ',
    'saldir: s',
    'Kaç: k',
    'Çık: q', sep='\n')
    hamle = input('\n> ')
    if hamle == 's':
        siz.saldir(rakip)
        print('Rakibinizin durumu')
        rakip.mevcut_durumu_görüntüle()
        print('Sizin durumunuz')
        siz.mevcut_durumu_görüntüle()
    elif hamle == 'k':
        siz.kaç()
    elif hamle == 'q':
        siz.oyundan_çık()