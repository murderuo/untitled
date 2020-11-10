import sqlite3
import  time


try:

    db_con=sqlite3.connect('kurlar.db')
    print("db oluşturuldu")
    if (db_con):
        print("bağlantı kuruldu")
        db_cur = db_con.cursor()
        try:
            db_cur.execute('''
            CREATE TABLE kurlar (
            sira INTEGER PRIMARY KEY AUTOINCREMENT,
            site VARCHAR,
            kur VARCHAR,
            alis VARCHAR,
            satis VARCHAR,
            zaman VARCHAR
            )
            ''')
            print("tablo oluşturuldu")
            db_con.commit()
            db_con.close()
        except:
            print("tablo oluşturulamadı veya tablo var.")

    else:
        print("baglantı kurulamadı")

except:
    print("db oluşturulamadı")


db_con = sqlite3.connect('kurlar.db')
db_cur = db_con.cursor()


def db_ekle(site, kur, alis, satis, zaman):
    db_con = sqlite3.connect('kurlar.db')
    db_cur = db_con.cursor()

    sorgu = 'INSERT INTO kurlar (site,kur,alis,satis,zaman) VALUES ('
    sorgu += '"' + site + '",'
    sorgu += '"' + kur + '",'
    sorgu += '"' + alis + '",'
    sorgu += '"' + satis + '",'
    sorgu += '"' + zaman + '")'
    # try:
    db_cur.execute(sorgu)
    db_con.commit()
        # print("veri eklendi")
        # db_con.close()

    # except:
    #     print("veri eklenemedi")
    db_con.close()
