from database import db


class ogrenci(db):
    def __init__(self):
        database_object = db()
        self.acilis()
        pass
    def acilis(self):
        print('''       ÖĞRENCİ OTOMASYONUNA HOŞ GELDİNİZ.''')
    def menu(self):
        print('''\n
        1-Öğrenci eklemek için      [E]
        2-Bölüm eklemek için        [B]
        3-Ders Eklemek İçin         [D]
        4-Not girmek için           [N]
        5-Kayıtları Listelemek için [K]
        6-Tabloları görmek için     [T]
        
        ##Çıkmak İçin [Ç]'ye basınız## ''')
        self.giris = input("Seçim :")

        return self.giris.upper()

object=ogrenci()



while 1:
    cevap = object.menu()
    if cevap=='E':
        kayitlar = object.kayit_listele('ogrenci').fetchall()
        for kayit in kayitlar:
            print("Öğrenci no: %s\tÖğrenci Adı:%s\tÖğrenci Soyadı:%s\tDers No:%s\tDers Adı:%s\tDevamsızlık:%s" % kayit)
        ad=input("öğrenci adını giriniz :")
        soyad=input("ögrenci soyadını giriniz :")
        bolum_n=input("Ders numarasını giriniz :")
        bolum_a=input("Ders adını giriniz :")
        devamsizlik=input("devamsızlık miktarı :")

        # ogr=ogrenci(ad,soyad,bolum_n,bolum_a,devamsizlik)
        # print(object.ogrenci_adi, " isimli ogrenci oluşturuldu")
        object.db_ogrenci_ekle(ad,soyad,bolum_n,bolum_a,devamsizlik)
        print("db eklendi")
        # cevap = object.menu()

    elif cevap=='B':
        kayitlar = object.kayit_listele('bolum').fetchall()
        # print(kayitlar)
        if kayitlar==False:
            print("kayıtlar getirilemedi")
        else:
            for kayit in kayitlar:
                print("Bölüm no:%s\tBölüm Adı:%s" % kayit)
        b_adi=input("Bölüm adını giriniz :")
        object.bolum_ekle(b_adi)
        print("Bölüm eklendi")
        # cevap = object.menu()b
    elif cevap=='D':
        kayitlar = object.kayit_listele('dersler').fetchall()
        if kayitlar==False:
            print(" tablo bulunamadı.")
        else:
            for kayit in kayitlar:
                print("Ders No: %s\tDers Adı: %s"%kayit)
        d_adi=input("Ders adını giriniz :")
        if object.ders_ekle(d_adi)==True: print("Ders eklendi")
        else: print("ders eklenemedi")
        # cevap = object.menu()
    elif cevap=='N':
        kayitlar=object.kayit_listele('notlar').fetchall()
        if kayitlar==False:
            print(" tablo bulunamadı.")
        else:
            for kayit in kayitlar:
                print("Ders no: %s\tDers Adı:%s\tÖğrenci No:%s\tÖğrenci Adı:%s\tÖğrenci Soyadı:%s\tÖğrenci Notu:%s" % kayit)

        ders_adi=input("Ders adını giriniz :")
        ogrenci_no=input("Öğrenci numarasını giriniz :")
        ogrenci_adi=input("Öğrenci adını giriniz :")
        ogrenci_soyadi=input("Öğrenci soyadını giriniz :")
        ogrenci_notu=input("Öğrenci notunu giriniz :")

        if object.not_ekle(ders_adi,str(ogrenci_no),ogrenci_adi,ogrenci_soyadi,str(ogrenci_notu))==True: print("not eklendi")
        # cevap = object.menu()

    elif cevap=='K':
        object.tablo_listele()
        t_adi=input('\nListelenecek tabloyu giriniz :')
        if t_adi=='notlar':
            kayitlar=object.kayit_listele(t_adi)
            # print("LİsTELEME DURUMU:",kayitlar)
            if kayitlar==False:
                print(t_adi," isimli tablo bulunamadı.")
            else:
                for kayit in kayitlar:
                    print("Ders no: %s\tDers Adı:%s\tÖğrenci No:%s\tÖğrenci Adı:%s\tÖğrenci Soyadı:%s\tÖğrenci Notu:%s" % kayit)
        elif t_adi=='bolum':
            kayitlar = object.kayit_listele('bolum').fetchall()
            # print(kayitlar)
            if kayitlar == False:
                print("kayıtlar getirilemedi")
            else:
                for kayit in kayitlar:
                    print("Bölüm no:%s\tBölüm Adı:%s" % kayit)
        elif t_adi=='dersler':
            kayitlar = object.kayit_listele('dersler').fetchall()
            if kayitlar == False:
                print(" tablo bulunamadı.")
            else:
                for kayit in kayitlar:
                    print("Ders No: %s\tDers Adı: %s" % kayit)

        elif t_adi=='ogrenci':
            kayitlar = object.kayit_listele('ogrenci').fetchall()
            if kayitlar == False:
                print(" tablo bulunamadı.")
            else:
                for kayit in kayitlar:
                    print("Öğrenci no: %s\tÖğrenci Adı:%s\tÖğrenci Soyadı:%s\tDers No:%s\tDers Adı:%s\tDevamsızlık:%s" % kayit)
        else:
            print("kayıtlar getirilemedi")
        # cevap = object.menu()

    elif cevap=='T':
        object.tablo_listele()

    elif cevap=='Ç':
        break




if __name__ == '__main__':
    ogrenci.acilis()
    ogrenci.menu()
























