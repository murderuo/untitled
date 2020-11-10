import sqlite3


class db():

    def __init__(self):
        self.conn = sqlite3.connect('ogrenci.db')
        self.cur = self.conn.cursor()
        if self.db_check() == True:

            try:
                self.cur.executescript('''
                CREATE TABLE ogrenci(
                ogrenci_no INTEGER PRIMARY KEY AUTOINCREMENT,
                ogrenci_ad TEXT,
                ogrenci_soyad TEXT,
                ogrenci_bolum_no TEXT,
                ogrenci_bolum TEXT,
                ogrenci_devamsizlik TEXT
                );
            
                CREATE TABLE bolum(
                bolum_no INTEGER PRIMARY KEY AUTOINCREMENT,
                bolum_adi TEXT
                );
             
         
                CREATE TABLE dersler(
                ders_no INTEGER PRIMARY KEY AUTOINCREMENT,
                ders_adi TEXT
                );
            
           
                CREATE TABLE notlar(
                ders_no INTEGER PRIMARY KEY AUTOINCREMENT,
                ders_adi TEXT,
                ogrenci_no TEXT,
                ogrenci_ad TEXT,
                ogrenci_soyad TEXT,
                ogrenci_not TEXT
                );
                
                ''')
                self.conn.commit()
                self.conn.close()
            except sqlite3.OperationalError:
                print("Aynı Tablodan Mevcut")
                # return False
                self.conn.close()

            else:
                # return True
                print("Tablolar oluşturuldu")

    def db_check(self):

        if (self.conn):
            # print("db bağlantısı kuruldu")
            # self.conn.close()
            return True
        else:
            # print("db bağlantısı kurulamadı")
            return False

    def db_ogrenci_ekle(self,isim, soyisim, bol_no, bol_ad,devamsizlik):

        # self.ogr_no=str(numara)
        self.ad=isim
        self.soyad=soyisim
        self.bolum_no=str(bol_no)
        self.bolum_ad=bol_ad
        self.ogrenci_devamsz=str(devamsizlik)

        self.values=(self.ad.upper(),self.soyad.upper(),self.bolum_no.upper(),self.bolum_ad.upper(),self.ogrenci_devamsz)
        self.conn=sqlite3.connect('ogrenci.db')
        self.cur=self.conn.cursor()
        self.sql = 'INSERT INTO ogrenci(ogrenci_ad,ogrenci_soyad,ogrenci_bolum_no,ogrenci_bolum,ogrenci_devamsizlik) ' \
                                'VALUES (?,?,?,?,?)'
        # print(self.sql)
        try:

            self.cur.execute(self.sql,self.values)
            self.conn.commit()

        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            return False
        else:
            self.conn.close()
            return True

    def bolum_ekle(self,b_adi):
        # self.bolum_no = str(b_no)
        self.bolum_ad = b_adi
        self.values = (self.bolum_ad.upper(),)
        self.conn = sqlite3.connect('ogrenci.db')
        self.cur = self.conn.cursor()
        self.sql = 'INSERT INTO bolum(bolum_adi) VALUES (?)'
        # print(self.sql)
        try:
            self.cur.execute(self.sql,self.values)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            self.conn.close()
            return False
        else:
            self.conn.close()
            return True

    def ders_ekle(self,ders_adi):

        # self.ders_no=str(ders_no)
        self.ders_ad=ders_adi
        self.values=(self.ders_ad.upper(),)
        self.sql = 'INSERT INTO dersler(ders_adi) VALUES (?)'
        self.conn = sqlite3.connect('ogrenci.db')
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(self.sql,self.values)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            return False
        else:
            self.conn.close()
            return True

    def not_ekle(self,ders_adi,ogrenci_no,ogrenci_adi,ogrenci_soyadi,ogrenci_notu):
        # self.ders_n=str(ders_no)
        self.ders_ad=ders_adi
        self.ogrenci_n=ogrenci_no
        self.ogrenci_ad=ogrenci_adi
        self.ogrenci_sadi=ogrenci_soyadi
        self.ogrenci_n=ogrenci_notu

        self.sql = 'INSERT INTO notlar(ders_adi,ogrenci_no,ogrenci_ad,ogrenci_soyad,ogrenci_not) VALUES (?,?,?,?,?)'
        self.values= (self.ders_ad.upper(),self.ogrenci_n,self.ogrenci_ad.upper(),self.ogrenci_sadi.upper(),self.ogrenci_n)
        self.conn = sqlite3.connect('ogrenci.db')
        self.cur=self.conn.cursor()
        try:
            self.cur.execute(self.sql,self.values)
            self.conn.commit()

        except sqlite3.IntegrityError:
            print("Aynı kayıttan mevcut")
            self.conn.close()
            return False
        else:
            self.conn.close()
            return True

    def kayit_listele(self,tablo_adi):

        self.tablo=tablo_adi
        self.sql="SELECT * FROM " +self.tablo

        try:
            self.conn = sqlite3.connect('ogrenci.db')
            self.cur = self.conn.cursor()
            self.data=self.cur.execute(self.sql)
            return self.data
        except:
            return False


    def tablo_listele(self):

        self.tablolar ='''SELECT * FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence' '''
        self.conn=sqlite3.connect('ogrenci.db')
        self.cur=self.conn.cursor()
        self.tables=self.cur.execute(self.tablolar)
        # return self.tables
        print("sistemde bulunan tablolar :")
        for self.tablo in self.tables:
            print('##',end='')
            print(self.tablo[1].upper(),end=' ')
