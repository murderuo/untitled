'''matbaa makinesi
mürekkep, şarj olayları olacak
mürekkep azalınca, mürekkep koyulacak
şarj kontrolü yapılacak azalırsa şarj edilecek
20 çalışmada bir dergi basacak
dergi çıkmadıysa derginin yüzde kaç olduğunu belirtecek
yeni dergi çıktığında kullanıcıdan ismi alınacak
basılan dergilerin sayısı tutulacak'''
import  random
import sys

class Makine:
    __cikan_dergiler=[]


    def __init__(self):
        self.murekkepmiktari=100
        self.sarji=100
        self.calismasayisi=0
    def calis(self):
        if self.murekkepKontrol() or self.sarjKontrol():
            self.murekkepsarfiyat=random.randint(1,7)
            self.sarjsarfiyat=random.randint(1,7)
            self.murekkepmiktari-=self.murekkepsarfiyat
            self.sarji-=self.sarjsarfiyat
            self.calismasayisi+=1  #calisma sayısını kontrol edip yeni dergi olayını yap
            if self.calismasayisi==20:
                self.yeniDergi()
                self.calismasayisi=0
            else:
                self.durum=self.dergiDurum()
                print("ilerleme {}".format(self.durum))

        else:
            print("Makine çalışamaz yeterli şarj veya murekkep yok")

    def murekkepKontrol(self):
        if self.murekkepmiktari<=10:
            print("murekkep azaldı murekkep doldurun")
            # print("makinenin murekkebi:",self.murekkepmiktari)
            return False
        else:
            print("makinenin murekkebi:",self.murekkepmiktari)
            return True

    def sarjKontrol(self):
        if self.sarji<=7:
            print("sarjı çok az şarj edin")
            # print("makinenin şarjı:",self.sarji)
            return False
        else:
            print("makinenin şarjı:",self.sarji)
            return  True

    def murekkepDoldur(self):
        self.karttus=random.randint(1,20)
        self.murekkepmiktari+=self.karttus
        print("murekkep dolduruldu")

    def sarjEt(self):
        self.sarj=random.randint(1,20)
        self.sarji+=self.sarj
        print("sar jedildi")

    def dergiDurum(self):
        self.yuzde=(self.calismasayisi/20)*100
        return self.yuzde

    def yeniDergi(self):
        print("yeni dergi çıktı isim verin")
        dergi_adi=input()
        Makine.__cikan_dergiler.append(dergi_adi)
        print("dergilere eklendi")
        self.dergileriGoster()

    def dergileriGoster(self):
        dergi_sayisi=len(Makine.__cikan_dergiler)
        dergiler=""
        for i in Makine.__cikan_dergiler:
            dergiler+=i + ", "
        print("Dergi sayısı: {}\n"
              "Dergiler: {}".format(dergi_sayisi,dergiler))

    def cikis(self):
        sys.exit()




if __name__=="__main__":

    makine=Makine()
    print("matbaamıza hoş geldiniz\n".upper())

    while True:
        print("makineyi çalıştırmak için [ç]\n"
              "sarj kontrol için [şk]\n"
              "murekkep kontrol için [mk]\n"
              "sarj etmek için [ş]\n"
              "murekkep eklemek için [m]\n"
              "dergileri göstermek icin [d]\n"
              "çıkmak için [e]\n".upper())
        secim=input()
        if secim=="ç":
            makine.calis()
        elif secim=="şk":
            makine.sarjKontrol()
        elif secim=="mk":
            makine.murekkepKontrol()
        elif secim=="ş":
            makine.sarjEt()
        elif secim=="m":
            makine.murekkepDoldur()
        elif secim=="d":
            makine.dergileriGoster()
        elif secim=="e":
            makine.cikis()
        else:
            print("geçersiz seçim\n")
