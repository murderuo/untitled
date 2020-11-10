import time #time modulu import
import os #os modulu ımport

class FileChecker: # dsya işlemlerimiz için class oluşturuyoruz

    def __init__(self):  # bu classtan bir örnek tanımladığımızda çalışacak fonksiyon
        self.file="comparewords.txt"
        if not os.path.exists(self.file): # self.file isimli dosyayı kontrol ediyoruz yoksa
            self.fileCreate()       #clasımızın filecreate fonksiyonunu çağırıyruz

    def fileCreate(self):
        with open(self.file,"a",encoding="utf-8") as file:         #self.isim dosyasını append modda aç
            file.write("                        COMPARED KEYWORDS\n")            #dosyaya yaz
            file.write("_____________________________________________________________\n")  #dosyaya yaz


    def fileOpenSave(self,comp_word):  #gelen self.file isimli parametreyi
        with open(self.file,"a",encoding="utf-8") as file:        #dosyayı append modda açarak
            file.write(comp_word+"\n")          #yaz

chcker=FileChecker()            #fileChecker sııfından chcker isimli bir örnek oluştur
book_file="book.txt" #kitabımız
word_file="words.txt" #wordlistimiz
with open(book_file,"r") as book,open(word_file,"r",encoding="utf-8") as words:#kitap dosyamızı ve wordlist dosyamısı  okuma modunda aç
    booklines=book.readlines()      #kitap dosyasındaki satırları oku
    wordlines=words.readlines()     #wordlist dosyasındaki satırları oku
    cnter=0                          #kitaptaki satırlarda tekrarlanan kelimeyi bulmak için sayaç oluşturuyoruz
    for wl in wordlines:            #wordlistte dönmeye başla, wl-->kelime oluyor,ilk kelimeyi alıyoruz
        for bl in booklines:        #kitabın ilk satırını alıyoruz
            if wl.strip() not in bl.lower().strip().split(): #wordlistteki ilk kelime, liste haline getirdiğimiz kitabın ilk satında yok mu? yoksa:
                cnter+=1        #kelime yok sayacı arttır
                print("word not found".format(wl.strip())) #uyarı
                #dönmeye devam et

        #yeni kelimeye geçiyoruz ve geçerken
        if cnter>1: #kelime sayacını kontrol et tekrarlı kelime sayısı 1 den büyükse:
            chcker.fileOpenSave(wl.strip())      #ckcker instance'ının dosyaya kaydet fonksiyonunu çalıştır
            print("added {}".format(chcker.file))  # eklendi uyarısını ver
            cnter=0 # sayacı sıfırla

