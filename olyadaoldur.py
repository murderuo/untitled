import random
import sys



class Player:
    def __init__(self,atackpw,hp,cntr):
        self.atackpower=atackpw
        self.hp=hp
        self.atackcounter=cntr


class Oyuncu(Player):
    def __init__(self,*args):
        super().__init__(*args)

    def saldir(self,dusman):
        if self.atackcounter==0: print("Şarjör yok, yeni şarjör yükle.")
        else:
            dusman.hp -=self.atackpower
            self.atackcounter-=1

        # if self.hp_kontrol()==False: sys.exit()

    def hp_kontrol(self):
        if self.hp<=0:
            print("Oyuncu öldü")
            self.hp=0
            return False
        else: return True

    @property
    def durumKontrol(self):
        print("****oyuncunun durumu****")
        print("oyuncunun atak gücü:{}\n"
              "oyuncunun canı: {}\n"
              "oyuncunun kalan kursunu:{}\n"
              .format(self.atackpower,self.hp,self.atackcounter))

class Dusman(Oyuncu):
    def __init__(self,*args):
        super().__init__(*args)


dusmanlar=[Dusman(random.randint(80,100),random.randint(80,100),5) for i in range(10)]
oyuncu=Oyuncu(150,4000,5)

while oyuncu.hp_kontrol():
    oyuncu.durumKontrol
    print("düşmanlar")
    for i in range(len(dusmanlar)):
        print(i+1,".düşmanın canı:",dusmanlar[i].hp)

    secim=input("hangi düşmana vurulacak")
    if int(secim)<=len(dusmanlar):

        oyuncu.saldir(dusmanlar[int(secim)-1])
        if dusmanlar[int(secim)-1].hp<0: dusmanlar.remove(dusmanlar[int(secim)-1])


        for i in dusmanlar:
            i.saldir(oyuncu)
        print(oyuncu.hp)







