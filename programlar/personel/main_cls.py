import db

class PersonelKayıt:
    per_data=n_data=[]

    def __init__(self):
        pass

    def pbilgileriAl(self):
        try:
            padi=input("Personelin Adı:")
            psoyadi=input("Personelin Soyadı:")
            ptcno=input("Personel Tc no:")
            if ptcno.isdigit():
                tc=int(float(ptcno))
            else:
                print("Tc no rakamlardan oluşmalı")
            podano=input("Personelin Oda Numarası :")
            if podano.isdigit():
                odano=int(float(podano))
            else:
                print("Oda no rakamlardan oluşmalı")
            pdahili=input("Dahili no:")
            if pdahili.isdigit():
                dah=int(float(pdahili))
            else:
                print("Oda no rakamlardan oluşmalı")
        except:
            print("Tc No/Oda No veya Dahili No\'da hata var. Lütfen kontrol ediniz.")
        return padi,psoyadi,tc,odano,dah


    # def getData(self):
    #     db_data=db.verial()
    #     for i in db_data:
    #         d["Adi"],d["soyadı"],d["TC No"],d["Oda No"],d["Dahili"]=i[0],i[1],i[2],i[3],i[4]
    #         # print(i)
    #         data.append(d)
    #         # print(d)
    #         d={}
    #     # print(d)
    #     return data





    # def listeyeAt(self,*args):
    #     value={}
    #     if len(args)!=5:
    #         value["Adi"],value["soyadı"],value["TC No"],value["Oda No"],value["Dahili"]=args[0][0],args[0][1],args[0][2],\
    #                                                                                args[0][3],args[0][4]
    #     else: print("girilen kaydı kontrol ediniz\n")
    #     self.n_data.append(value)
    #     self.p_ekranaYadir(value)


    # def p_ekranaYadir(self,entry):
    #     print("Adı:{}\t\t\t\tSoyadı:{}\t\t\t\tTc No:{}\t\t\t\tOda No:{}\t\t\t\tDahili:{}\n".format(entry["Adi"],
    #                                                                                                entry["soyadı"],
    #                                                                                                entry["TC No"],
    #                                                                                                entry["Oda No"],
    #                                                                                                entry["Dahili"]))


    # def personelleriGoster(self,liste):
    #     print("Adı:\t\t\t\tSoyadı:\t\t\t\tTc No:\t\t\t\tOda No:\t\t\t\tDahili:\n")
    #     print("-----------------------------------------------------------------")
    #     for i in liste:
    #         print("{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\n".format(i["Adi"],i["soyadı"],i["TC No"],i["Oda No"],
    #                                                                     i["Dahili"]))

    # def kayitSil(self,data):
    #     self.tumpersoneliGoster(data)
    #     print("Kayıt Sayısı:{}".format(len(data)))
    #     secim=int(input("Hangi Kaydı Sileceksiniz ?:"))
    #     data.remove(data[secim-1])








if __name__ == '__main__':
    baslik="Personel Kayıt Programına Hoş Geldiniz"
    print("-"*10,baslik,"-"*10,sep="")
    print("-"*(len(baslik)+20),sep="")
    # while True:

# Yeni personel ekle
# tüm personelleri göster
# kayıt sil
# kayıt değiştir
# çıkış yap





