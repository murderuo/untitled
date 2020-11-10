import sqlite3
import  time
try:
    db_con=sqlite3.connect('personel.db')
    # print("db oluşturuldu")
    if (db_con):
        # print("bağlantı kuruldu")
        db_cur = db_con.cursor()
        try:
            db_cur.execute('''
            CREATE TABLE personel (
            sira INTEGER PRIMARY KEY AUTOINCREMENT,
            adi VARCHAR,
            soyadi VARCHAR,
            tc INTEGER ,
            odano INTEGER ,
            dahili INTEGER 
            )
            ''')
            print("tablo oluşturuldu")
            db_con.commit()
            db_con.close()
        except:
            print("tablo oluşturulamadı veya tablo var.")
except:
    print("db ok")


# db_con = sqlite3.connect('personel.db')
# db_cur = db_con.cursor()


def db_ekle(lst):
    db_con=sqlite3.connect('personel.db')
    db_cur=db_con.cursor()
    for i in lst:
        adi,soyadi,tc,odano,dahili=i["Adi"],i['soyadı'],i['TC No'],i['Oda No'],i['Dahili']
        sorgu="""INSERT INTO personel (adi,soyadi,tc,odano,dahili) 
                VALUES ("{}","{}",{},{},{})""".format(adi,soyadi,tc,odano,dahili)
        try:
            db_cur.execute(sorgu)
            db_con.commit()
        except:
            print("db eklenemedi")
            db_con.close()
            break
    print("db eklendi")
    db_con.close()

def verial():
    db_con=sqlite3.connect('personel.db')
    db_cur=db_con.cursor()
    sorgu="""SELECT DISTINCT adi,soyadi,tc,odano,dahili FROM personel"""
    data=db_cur.execute(sorgu)
    exec=data.fetchall()
    db_con.commit()
    db_con.close()
    return exec




# db_ekle(lst)