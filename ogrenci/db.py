import sqlite3


class db():

    def __init__(self):
        # self.ogr_no = 0
        # self.ad = ''
        # self.soyad =''
        # self.bolum_no = 0
        # self.bolum_ad = ''
        # self.ders_no = 0
        # self.ders_adi = ''
        # self.ogr_not = ''

        self.conn = sqlite3.connect('ogrenci.db')
        self.cur = self.conn.cursor()
        if self.db_check() == True:

            try:
                self.cur.execute('''
                CREATE TABLE ogrenci(
                ogrenci_no INTEGER PRIMARY KEY AUTOINCREMENT,
                ogrenci_ad TEXT,
                ogrenci_soyad TEXT,
                ogrenci_bolum_no TEXT,
                ogrenci_bolum TEXT
                
                )
                ''')
                self.cur.execute('''
                CREATE TABLE bolum(
                bolum_no INTEGER PRIMARY KEY AUTOINCREMENT,
                bolum_adi TEXT
                )
                ''')
                self.cur.execute('''
                CREATE TABLE dersler(
                ders_no INTEGER PRIMARY KEY AUTOINCREMENT,
                ders_adi TEXT
                )
                ''')
                self.cur.execute('''
                CREATE TABLE notlar(
                ders_no INTEGER,
                ders_adi TEXT,
                ogrenci_no TEXT,
                ogrenci_ad TEXT,
                ogrenci_soyad TEXT,
                ogrenci_not TEXT
                )
                
                ''')
                self.conn.commit()
                self.conn.close()
            except sqlite3.OperationalError:
                print("Aynı Tablodan Mevcut")
            else:
                print("Tablolar oluşturuldu")

    def db_check(self):

        if (self.conn):
            # print("db bağlantısı kuruldu")
            # self.conn.close()
            return True
        else:
            print("db bağlantısı kurulamadı")
            return False

    def db_ogrenci_ekle(self,numara,isim, soyisim, bol_no, bol_ad):

        self.ogr_no=numara
        self.ad=isim
        self.soyad=soyisim
        self.bolum_no=bol_no
        self.bolum_ad=bol_ad
        self.conn=sqlite3.connect('ogrenci.db')
        self.cur=self.conn.cursor()
        self.sql = 'INSERT INTO ogrenci(ogrenci_no,ogrenci_ad,ogrenci_soyad,ogrenci_bolum_no,ogrenci_bolum) VALUES ('
        self.sql += str(self.ogr_no) + ','
        self.sql += '"' + self.ad + '",'
        self.sql += '"' + self.soyad + '",'
        self.sql += str(self.bolum_no) + ','
        self.sql += '"' + self.bolum_ad + '")'
        print(self.sql)
        try:

            self.cur.execute(self.sql)
            self.conn.commit()

        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            return False
        else:
            self.conn.close()
            return True


    def bolum_ekle(self,b_no,b_adi):
        self.bolum_no = str(b_no)
        self.bolum_ad = b_adi
        self.conn = sqlite3.connect('ogrenci.db')
        self.cur = self.conn.cursor()
        self.sql = 'INSERT INTO bolum(bolum_no,bolum_adi) VALUES ('
        self.sql += self.bolum_no + ','
        self.sql += '"' + self.bolum_ad + '")'
        print(self.sql)
        try:
            self.cur.execute(self.sql)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            return False
        else:
            self.conn.close()
            return True

    def ders_ekle(self,ders_no,ders_adi):

        self.ders_no=str(ders_no)
        self.ders_adi=ders_adi
        self.conn = sqlite3.connect('ogrenci.db')
        self.cur = self.conn.cursor()
        self.sql = 'INSERT INTO bolum(bolum_no,bolum_adi) VALUES ('
        self.sql += self.ders_no + ','
        self.sql += '"' + self.ders_adi + '")'

        try:
            self.cur.execute(self.sql)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            return False
        else:
            self.conn.close()
            return True

    def not_ekle(self,ders_no,ders_adi,ogrenci_no,ogrenci_adi,ogrenci_soyadi,ogrenci_notu):
        self.ders_no=str(ders_no)
        self.ders_adi=ders_adi
        self.ogrenci_no=str(ogrenci_no)
        self.ogrenci_adi=ogrenci_adi
        self.ogrenci_soyadi=ogrenci_soyadi
        self.ogrenci_notu=str(ogrenci_notu)

        self.sql = 'INSERT INTO notlar(ders_no,ders_adi,ogrenci_no,ogrenci_ad,ogrenci_soyad,ogrenci_not) VALUES ('
        self.sql += self.ders_no + ','
        self.sql += '"' + self.ders_adi + '",'
        self.sql += self.ogrenci_no + ','
        self.sql += '"' + self.ogrenci_adi + '",'
        self.sql += '"' + self.ogrenci_soyadi + '",'
        self.sql += self.ogrenci_notu + ')'
        try:

            self.cur.execute(self.sql)
            self.conn.commit()

        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            return False
        else:
            self.conn.close()
            return True

    def kayit_listele(self,tablo_adi):

        self.tablo=tablo_adi
        self.sql='SELECT * FROM ' +self.tablo
        try:
            self.conn = sqlite3.connect('ogrenci.db')
            self.cur = self.conn.cursor()
            self.data=self.cur.execute(self.sql)
        except:
            return False
        else:
            return self.data












db=db()
# ogrenci=db.db_ogrenci_ekle(4,'sinem','durmaz',3,'biyoloji')
# print(ogrenci)
# bolum=db.bolum_ekle(3,'biyoloji')
# print(bolum)
sonuc=db.kayit_listele('ogrenci')

print("Öğrenci numarası\t#Öğrenci Adı\t#Öğrenci Soyası\t#Ders numarsı\t#Ders Adı")
for kayit in sonuc.fetchall():
    print("\t%s\t\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t\t%s" % kayit)

