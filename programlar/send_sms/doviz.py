import requests
from bs4 import BeautifulSoup
import time
import locale


locale.setlocale(locale.LC_ALL, 'turkish')


def dovizcom():

    url= "http://www.doviz.com"
    r= requests.get(url)
    icerik=BeautifulSoup(r.content,"lxml")
    all_Li=icerik.find("ul")
    li=all_Li.find_all("li")

    item=0
    # print("DOVİZ.COM FİYATLARI:")
    b=[]
    f=[]

    for oneLi in li:
        link=oneLi.find("a")
        baslik=link.find("span",attrs={"class":"menu-row1"}).text
        fiyat=link.find("span",attrs={"class":"menu-row2"}).text
        degisim=link.find("span",attrs={"class":"menu-row3"}).text
        # print(baslik,fiyat,degisim,sep="  ")
        b.append(baslik)
        f.append(fiyat)
        item+=1
        if item ==3: return b, f
        elif item==4: break


def enparacom():

    url= "https://www.qnbfinansbank.enpara.com/doviz-kur-bilgileri/doviz-altin-kurlari.aspx"
    r= requests.get(url)
    icerik=BeautifulSoup(r.content,"lxml")
    table=icerik.find("div",attrs={"id":"pnlContent"})
    spans=table.find_all("span")
    # print("\nENPARA.COM FİYATLARI:")
    b=[]
    f_a=[]
    f_s=[]
    item=0
    for span in spans:
        dls=span.find_all("dl")
        for dl in dls:
            item+=1
            # print(dl.dt.text,dl.dd.text,dl.dd.next_sibling.text)

            b.append(dl.dt.text)
            f_a.append(dl.dd.text)
            f_s.append(dl.dd.next_sibling.text)
        if item==3:
            break
    return b, f_a, f_s


# syc = 0
# while 1:
#
#
#     try:
#         print("-"*30)
#         basliklar, fiyatlar = dovizcom()
#         basliklar_enp, a_fiyatlar_enp, s_fiyatlar_enp = enparacom()
#         print("-"*30)
#         print(time.strftime("%c"))
#     except:
#         print("Veri okunamadı")
#         time.sleep(2)
#         # break
#     else:
#         syc += 1
#         if syc == 6:
#             try:
#                 for i in range(3):
#                     db.db_ekle("doviz.com",basliklar[i],"",fiyatlar[i],time.strftime("%X"))
#                     time.sleep(0.5)
#                     db.db_ekle("enpara.com",basliklar_enp[i],a_fiyatlar_enp[i],s_fiyatlar_enp[i],time.strftime("%X"))
#
#                 print("db eklendi")
#             except:
#                 print("db eklenemedi")
#             syc=0
#
#     time.sleep(20)
#
#
#
#

	
#https://belgeler.yazbel.com/python-istihza/standart_moduller/time.html

# datetime modülünü incelerken gördüğümüz tarih biçimlendiricileri time modülü için de geçerlidir:

# %a:	hafta gününün kısaltılmış adı
# %A:	hafta gününün tam adı
# %b:	ayın kısaltılmış adı
# %B:	ayın tam adı
# %c:	tam tarih, saat ve zaman bilgisi
# %d:	sayı değerli bir karakter dizisi olarak gün
# %j:	belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
# %m:	sayı değerli bir karakter dizisi olarak ay
# %U:	belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı
# %y:	yılın son iki rakamı
# %Y:	yılın dört haneli tam hali
# %x:	tam tarih bilgisi
# %X:	tam saat bilgisi
    
