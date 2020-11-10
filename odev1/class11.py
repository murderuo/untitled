class Firma:
    firmalar=[]
    gelirler=[]
    data={}

    def __init__(self):
        pass

    def firmaAl(self):
        self.firma_s=int(input("kac firma girilecek:"))
        for i in range(self.firma_s):
            print(i+1,". firmanın ismini giriniz:",end="")
            self.firma=input()
            self.firma=self.firma.strip()
            Firma.firmalar.append(self.firma)

    def gelirAl(self):
        for i in range(self.firma_s):
            print(i+1,". firmanın gelirlerini birer boşluk bırakarak giriniz:",end="")
            self.income=input()
            self.income=self.income.strip()
            self.incomes=self.inteCevir(self.income)
            Firma.gelirler.append(self.incomes)
            Firma.data[Firma.firmalar[i]]=self.modFreq(self.incomes)

    def inteCevir(self,strIncome):
        v=[]
        strIncome=strIncome.split(" ")
        for i in strIncome:
            v.append(int(i))
        # self.modFreq(v)
        return v

    def modFreq(self,incomes):
        mods_freqs=[]
        mod_fre={}
        syc=0
        for i in self.incomes:
            if i in mod_fre.keys():
                syc=mod_fre[i][1]  # print(syc)
            if i in self.incomes:
                syc+=1
                mod_fre[i]=i,syc
                syc=0
        keys=mod_fre.keys()
        fre=[]
        for i in mod_fre.values():
            fre.append(i[1])
        for i in mod_fre.values():
            if i[1] == max(fre):
                # print("mod/frekans:",i)
                return list(i)
                break
    def ortalamalariBul(self):
        self.value_list=list(Firma.data.values())
        # print(self.value_list)
        mod_ort=0
        freq_ort=0

        for i in self.value_list:
            mod_ort+=i[0]
            freq_ort+=i[1]

        mod_ort=mod_ort/self.firma_s
        freq_ort=freq_ort/self.firma_s
        return mod_ort,freq_ort

firma=Firma()
# yeniliste=firma.inteCevir('10 20 30 50 50 50 50 40')
# print(yeniliste)
firma.firmaAl()
firma.gelirAl()
print("Data:",Firma.data)
mod_ort,freq_ort=firma.ortalamalariBul()
print("Girilen veri kümesi:",Firma.data)
print("Girilen verinin mod değerlerinin ortalaması:",mod_ort)
print("Girilen verinin frekans değerlerinin ortalaması:",freq_ort)
