import sqlite3


baglanti=sqlite3.connect("sozluk.db")

#if baglanti:
#    print("veri tabanı oluşturuldu, bağlantı gerçekleştirildi")
#else:
#    print("hata var")

konum=baglanti.cursor()


#tablo oluşturma

#konum.execute('''
#create table sozluk (
#kelime_sira integer(3) primary key,
#kelime_tr varchar(15),
#kelime_en varchar(15)
#)
#''')

#oluşturulan tabloya veri girme

try:
    konum.execute("INSERT INTO sozluk(kelime_en,kelime_tr) values('room','oda')")

except:

    print("kayıt edilemedi")

baglanti.commit()
baglanti.close()