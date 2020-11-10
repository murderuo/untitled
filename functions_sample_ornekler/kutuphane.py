import sqlite3
import  time

baglanti=sqlite3.connect("k.db")
konum=baglanti.cursor()

def veriekle_kitap(tablo_adi,alan_adlari,veriler):


    sorgu='INSERT INTO '+tablo_adi+'('
    sorgu+=str(alan_adlari)+') VALUES ('
    sorgu=sorgu.replace("[",'')
    sorgu=sorgu.replace("]","")
    sorgu=sorgu.replace("'","")
    sorgu+=str(veriler)+')'
    sorgu = sorgu.replace("[", '')
    sorgu = sorgu.replace("]", "")

    print("veri ekleniyor")
    time.sleep(1)
    try:

        konum.execute(sorgu)
        baglanti.commit()
        print(sorgu," sorgusu eklendi ...")
    except:
        print("hata,veri eklenemedi")



    #sorgu='INSERT INTO '+tablo_adi+'('
#
    #for alan_adi in alan_adlari:
    #    sorgu+=alan_adi
    #    sorgu+=','
    #sorgu+=') VALUES ('
#
    #for veri in veriler:
    #    sorgu+='"'+veri+'"'
    #    sorgu+=','
    #sorgu+=')'
    #print(sorgu)





if baglanti:

    print("bağlantı kuruldu")
    time.sleep(1)
    try:
        konum.execute('''CREATE TABLE kitaplar (
        kitap_no INTEGER PRIMARY KEY,
        kitap_adi VARCHAR (15),
        kitap_kategori INTEGER(2)    
        )''')
    except:
        print("kitaplar tablosu var")
    else:
        print("tablo oluşturuldu")

    try:
        konum.execute('''CREATE TABLE kategoriler (
        kategori_no INTEGER(2) PRIMARY KEY,
        kategori_adi VARCHAR(15)          
        )''')
    except:
        print("kategori tablosu var")
    else:
        print("kategori tablosu oluşturuldu")

    try:
        konum.execute('''CREATE TABLE calisanlar(
        calisan_no INTEGER(3) PRIMARY KEY,
        calisan_adi VARCHAR(10),
        calisan_maas VARCHAR(10)                  
        )''')
    except:
        print("çalışan tablosu var")
    else:
        print("çalışan tablosu oluşturuldu")





else:
    print("hata alındı")


# def veriekle_calisan(tablo_adi,ad,maas):
#
#     sorgu='INSERT INTO '+tablo_adi
#     sorgu+='('+ad+



def tablo_sec():

    tablolar=konum.execute('''SELECT * FROM sqlite_master WHERE type = 'table' AND 
                                          
                                         name != 'sqlite_sequence'
    ''')

    # print(tablolar)
    print("sistemde bulunan tablolar :")
    for tablo in tablolar:
        print(tablo[1])



    tablo_adi = input("giriş yapılacak tabloyu giriniz :")

    alanlar=konum.execute('SELECT column_name FROM '+tablo_adi+';')

    print("eklenecek alanlar :")








# tablo_alanlari=["kitap_adi","kitap_kategori"]
# kitaplar=["su adamı","bilim kurgu"]
#
# veriekle_kitap(tablo_adi,tablo_alanlari,kitaplar)



tablo_sec()

baglanti.commit()
baglanti.close()
