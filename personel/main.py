import db

def veriCek():
    d={}
    data=[]
    db_data=db.verial()
    for i in db_data:
        d["Adi"],d["soyadı"],d["TC No"],d["Oda No"],d["Dahili"]=i[0],i[1],i[2],i[3],i[4]
        # print(i)
        data.append(d)
        # print(d)
        d={}
    # print(d)
    return data
per_data=veriCek()
n_data=[]
print(per_data)
print(n_data)


def pbilgileriAl():
    padi=input("Personelin Adı:")
    psoyadi=input("Personelin Soyadı:")
    ptcno=int(input("Personel Tc no:"))
    podano=int(input("Personelin Oda Numarası :"))
    pdahili=int(input("Dahili no:"))
    return padi,psoyadi,ptcno,podano,pdahili

def listeyeAt(*args):
    dict={}
    dict["Adi"],dict["soyadı"],dict["TC No"],dict["Oda No"],dict["Dahili"]=args[0][0],args[0][1],args[0][2],args[0][3],args[0][4]
    n_data.append(dict)
    p_ekranaYadir(dict)

def p_ekranaYadir(dict):

    print("Adı:{}\t\t\t\tSoyadı:{}\t\t\t\tTc No:{}\t\t\t\tOda No:{}\t\t\t\tDahili:{}\n".format(dict["Adi"],dict["soyadı"],
                                                                                             dict["TC No"],
                                                                                             dict["Oda No"],
                                                                                             dict["Dahili"]))

def tumpersoneliGoster(liste):
    print("Adı:\t\t\t\tSoyadı:\t\t\t\tTc No:\t\t\t\tOda No:\t\t\t\tDahili:\n")
    for i in liste:
        print("{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\n".format(i["Adi"],i["soyadı"],i["TC No"],i["Oda No"],i["Dahili"]))

def kayitSil(data):
    tumpersoneliGoster(data)
    print("Kayıt Sayısı:{}".format(len(data)))
    secim=int(input("Hangi Kaydı Sileceksiniz ?:"))
    data.remove(data[secim-1])


if __name__ == '__main__':
    print(""" Personel kayıt programına hoş geldiniz.""")
    psayisi=int(input("kac personel girilecek: "))
    for i in range(psayisi):
        listeyeAt(pbilgileriAl())
    if input("db eklensin mi [e]:")=="e":
        db.db_ekle(n_data)
    all_data=per_data+n_data
    kayitSil(all_data)
    print("#"*15)
    tumpersoneliGoster(all_data)
    print(len(all_data))

