


class makine():
    def __init__(self):
        self.sarji =87
        self.mürekkebi=87
        self.calismasayisi=0
        self.yuzde=0
        self.dergisayisi=0
        self.dergiler=[]

    def dergiuret(self):
        if (self.mürekkebi<=0 or self.sarji<=0):
            print("dergi üretilemiyor")
            print("sarjını ya da mürekkebini kontrol edin")
            print("*"*15)
            #print(self.durum())
        else:


            self.calismasayisi+=1
            self.mürekkebi-=8
            self.sarji-=15



            if (self.calismasayisi %20==0):
                print("yeni dergi çıktı")
                self.dergiler.append(input("yeni dergiye isim vermek ister misiniz"))
                self.calismasayisi=0
                self.dergisayisi+=1
                #print("sarji :",self.sarji)
                #print("murekkebi :",self.mürekkebi)
            else:
                self.yuzde=(self.calismasayisi/20)*100
                print("derginin çıkmasına yüzde",self.yuzde,"var")
                #print("sarji :", self.sarji)
                #print("murekkebi :", self.mürekkebi)




        #else:
         #   self.dergiuret()

    def mürekkepkontrol(self):
        print("şu anki mürekkep miktarı :",self.mürekkebi)
        if self.mürekkebi<=1:
            self.mürekkepkoy()
        return self.mürekkebi

    def sarjkontrol(self):
        print("şu anki şarjı :",self.sarji)
        if self.sarji<=1:
            self.sarjet()
        return  self.sarji

    def sarjet(self):
        self.sarji+=25
        print("şarj edildi.şarjı :",self.sarji)

    def mürekkepkoy(self):
        self.mürekkebi+=25
        print("mürekkep koyuldu.mürekkebi :", self.mürekkebi)

    def durum(self):

        print("*"*15)
        print("üretilen dergi sayısı :",len(self.dergiler))
        print("dergi isimleri",self.dergiler)
        #print("çalışma sayısı: ",self.calismasayisi)
        print("*" * 15)

print("dergi üretim programına hoş geldiniz.")
cvp=input("\ndergi üretmeye başlayalım mı?[E/H]:")
dergimak=makine()
#dergimak.durum()
while(cvp=='e'):

    dergimak.dergiuret()

    mürekkepseviyesi=dergimak.mürekkepkontrol()
    sarjseviyesi=dergimak.sarjkontrol()

    if mürekkepseviyesi<=0:
        dergimak.mürekkepkoy()
        #dergimak.durum()
    elif sarjseviyesi<=0:
        dergimak.sarjet()
        #dergimak.durum()



    cvp = input("\ndergi üretmeye devam edelim mi?[E/H]:")
    if cvp=='h':
        dergimak.durum()

        break
