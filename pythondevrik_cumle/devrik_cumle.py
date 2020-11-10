import random


class Devrik_cumle:
    n=[",",".","?","!","...","'"]
    d_cumle=[]
    y_cumle=""
    def __init__(self,cumle):
        self.ncumle=cumle.strip()
        self.kelimeler=self.ncumle.split()
        self.kontrolEt(self.kelimeler)

    def kontrolEt(self,kelimeler):
        for k in kelimeler:
            if len(k) <= 3 or (k[-1] in Devrik_cumle.n and len(k) <= 4):
                Devrik_cumle.d_cumle.append(k)
            elif k[-1]+k[-2]+k[-3] in Devrik_cumle.n:
                self.ucnokta=self.ucNoktaBul(k)
                if self.ucnokta == k:
                    self.ucnokta=self.ucNoktaBul(k)
                    Devrik_cumle.d_cumle.append(self.ucnokta)
                else:
                    Devrik_cumle.d_cumle.append(self.ucnokta)

            elif len(k) > 3 and k[-1] in Devrik_cumle.n:
                self.noktalamali=self.noktalamaBul(k)
                if self.noktalamali == k:
                    self.noktalamali=self.noktalamaBul(k)
                    Devrik_cumle.d_cumle.append(self.noktalamali)
                else:
                    Devrik_cumle.d_cumle.append(self.noktalamali)

            elif len(k) >= 4:
                self.normalkelime=self.kelimeKaristir(k)
                if self.normalkelime == k:
                    self.normalkelime=self.kelimeKaristir(k)
                    Devrik_cumle.d_cumle.append(self.normalkelime)
                else:
                    Devrik_cumle.d_cumle.append(self.normalkelime)
    def ucNoktaBul(self,klme3):
        d_kelime=klme3[0]
        kortasi=list(klme3[1:-3])
        random.shuffle(kortasi)
        for ortadakiharf in kortasi:
            d_kelime+=ortadakiharf
        d_kelime+=klme3[-4]+klme3[-1]+klme3[-2]+klme3[-3]

        return d_kelime
    def noktalamaBul(self,klme):
        d_kelime=klme[0]
        kortasi=list(klme[1:-2])
        random.shuffle(kortasi)
        for ortadakiharf in kortasi:
            d_kelime+=ortadakiharf
        d_kelime+=klme[-2]+klme[-1]
        return d_kelime
    def kelimeKaristir(self,klme2):
        d_kelime=klme2[0]
        kortasi=list(klme2[1:-1])
        random.shuffle(kortasi)
        for ortadakiharf in kortasi:
            d_kelime+=ortadakiharf
        d_kelime+=klme2[-1]

        return d_kelime
    def yeniCumle(self):
        for k in Devrik_cumle.d_cumle:
            Devrik_cumle.y_cumle+=k+" "
        print(Devrik_cumle.y_cumle)

if __name__=="__main__":

    cumle=input("cumleyi giriniz:")
    yenicumle=Devrik_cumle(cumle)
    yenicumle.yeniCumle()


