from personel_class.db_class import database_tool as db
import sys

class PersonelKayit(db):
    def __init__(self,*args):
        # super().__init__(*args)
        self._padi=""
        self._psoyadi=""
        self._ptcno=""
        self._podano=""
        self._pdahili=""
        self._my_args=""
        self._db_name="database.db"

    def dbBilgileriniAl(self):
        while True:
            print("1 adet db,1 adet tablo adı ve 5 alan adı giriniz.")
            dbname=input("veritabanı ismini giriniz")
            tablename=input("tablo adını giriniz:")
            clmn1=input("1.alan adı")
            clmn2=input("2.alan adı")
            clmn3=input("3.alan adı")
            clmn4=input("4.alan adı")
            clmn5=input("5.alan adı")
            my_args=(dbname,tablename,clmn1,clmn2,clmn3,clmn4,clmn5,)
            if len(my_args) != 7:
                print("Lütfen eksik bilgi girmeyiniz")
                continue
            for i in my_args:
                if not i.isalpha():
                    print("Değerleri girerken sadece  [a-z / A-Z] kullanınız.")
                    continue
            break
        return my_args


    def pbilgileriAl(self):
        try:
            self._padi=input("Personelin Adı:")
            self._psoyadi=input("Personelin Soyadı:")
            self._ptcno=input("Personel Tc no:")
            self._podano=input("Personelin Oda Numarası :")
            self._pdahili=input("Dahili no:")
            self._my_args=(self._padi,self._psoyadi,self._ptcno,self._podano,self._pdahili,)
            return self._my_args
        except:
            print("hata var. Lütfen kontrol ediniz.")

    def cikis(self):
        print("çıkış yapıldı")
        sys.exit()


if __name__ == '__main__':
    per_tool=PersonelKayit()

    # baslik="Personel Kayıt Programına Hoş Geldiniz"
    # print("-"*10,baslik,"-"*10,sep="")
    # print("-"*(len(baslik)+20),sep="")
    # print("kayıtlı db yok,db oluşturulacak")
    # dbvalues=per_tool.db_olustur()
    # db_Tool=db(*dbvalues)
    # stat=db_Tool.createTable()

    while True:
        print("""   
                    1)db oluştur
                    2)Yeni personel ekle
                    3)tüm personelleri göster
                    4)kayıt sil
                    5)kayıt değiştir
                    6)çıkış yap
                    """)
        inpt=input("Seçiminiz:")
        if inpt.isdigit():
            if inpt=="1": #todo database crate selection
                dbargs=per_tool.dbBilgileriniAl()
                print(dbargs)
                stat1=per_tool.get_dbValues(*dbargs)
                # stat1=per_tool.createTable()
                # per_tool.dbConnect()
                # per_tool.dbClose()
                if stat1 == True:
                    print("db oluşturuldu")
                else:
                    print("db oluşturulamadı")
                    sys.exit()

            elif inpt=="2":
                values=per_tool.pbilgileriAl()
                print(values)
                stat=per_tool.insertValue(values)
                print(stat)
            elif inpt=="3":
                print(per_tool.getallValues())
            elif inpt=="4":
                print(per_tool.getallValues())
                secim=input("silinecek kayıt numarasını giriniz:")
                if secim.isdigit():
                    stat=per_tool.deleteEntry(secim)
                    if stat == True: print("personel silindi")
                    else: print("hata")
                else: print("hatalı sıra no")
            elif inpt=="5":
                print(per_tool.getallValues())
                secim=input("güncellecek kayıt numarasını giriniz:")
                print("yeni bilgileri giriniz")
                new_args=per_tool.pbilgileriAl()
                if secim.isdigit():
                    per_tool.updateselectedValue(secim,new_args)
                else:
                    print("hatalı sıra no")
            elif inpt=="6":
                per_tool.cikis()