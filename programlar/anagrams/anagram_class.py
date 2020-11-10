

class AnagramFind():
    def __init__(self):
        self._tmp=[]
        self._seperated={}


    def check(self,liste):
        for k in liste:  # kelimeler listesi içinde döngümüzü başlatıyoruz
            k_list=list(k)  # gelen k string'ini liste haline getirip k_list değerine atıyoruz k_list=["d","e","l","t","a","s"]
            k_list.sort()  # k_list isimli iste elemlarını sıralıyoruz  ['a', 'd', 'e', 'l', 's', 't']
            for j in liste:  # kelimeler listesinde yeni bir döngü başlatıyoruz
                j_list=list(j)  # gelen j değerini liste yapıp j_list içine atıyoruz j_list=["d","e","l","t","a","s"]
                j_list.sort()  # j_list listesini sıralıyoruz ['a', 'd', 'e', 'l', 's', 't']
                if k_list == j_list:  # k_list ve j_list listelerini karşılaştırıyoruz
                    self._tmp.append(j)  # dğerler aynıysa tmp listesine j değişkenimizi atıyoruz
            self._seperated[k]=self._tmp  # j değişkeni kelimelerde döndükten sonra çıkışta datalarımızı atacağımız sözlüğe tmp listemizi ekliyoruz
            self._tmp=[]  # yeni bir k değeri içim tm

            # p listemizi boşaltıyoruz.

    def allValues(self):
        return list(self._seperated.values())

    def removeDublicateAndAloneSimple(self):  # values değişkeninde bulunan birden fazla kayıdı ve 1 adet kayıtları olan değerleri siliyoruz
        f_list=[]  # uniq kayıtları tutacak liste
        for l in self.allValues():  # gelen list parametresinde dönü kuruyoruz
            if len(l) > 1:  # l değişkeninin değeri 1 den büyükse:
                if l not in f_list:  # uniq kayıtları tutacak listede yoksa
                    f_list.append(l)  # uniq kayıtları tutacak listeye ekle
        return f_list  # uniq kayıtları tutacak listeyi geri gönder

    def printValues(self):
        for v in self.removeDublicateAndAloneSimple():
            print(v)

if __name__ == '__main__':
    kelimeler=['deltas','desalt','lasted',"salted","slated",'mehmet',"staled",'retainers',"yetisin","ternaries","cs101",
               "generating","greatening","python","resmelts","smelters","termless","istinye"]

    bul=AnagramFind()
    bul.check(kelimeler)
    bul.printValues()





