import requests
from bs4 import BeautifulSoup
import time
import locale


locale.setlocale(locale.LC_ALL, 'turkish')


while 1:

	def dovizcom():
	    url= "http://www.doviz.com"

	    r= requests.get(url)
	    icerik=BeautifulSoup(r.content,"lxml")



	    all_Li=icerik.find("ul")
	    li=all_Li.find_all("li")

	    item=0
	    print("DOVİZ.COM FİYATLARI:")
	    for oneLi in li:
	            
	        link=oneLi.find("a")
	        baslik=link.find("span",attrs={"class":"menu-row1"}).text
	        fiyat=link.find("span",attrs={"class":"menu-row2"}).text
	        degisim=link.find("span",attrs={"class":"menu-row3"}).text
	        print(baslik,fiyat,degisim,sep="  ")
	        item+=1
	        if item ==4:
	            break

	def enparacom():

	    
	    url= "https://www.qnbfinansbank.enpara.com/doviz-kur-bilgileri/doviz-altin-kurlari.aspx"

	    r= requests.get(url)
	    icerik=BeautifulSoup(r.content,"lxml")
	   

	    table=icerik.find("div",attrs={"id":"pnlContent"})
	    #print(table)
	    spans=table.find_all("span")
	    print("\nENPARA.COM FİYATLARI:")
	    for span in spans:
	        dls=span.find_all("dl")
	        for dl in dls:
	            print(dl.dt.text,dl.dd.text,dl.dd.next_sibling.text)

	print("-"*30)
	dovizcom()

	enparacom()
	print("-"*30)
	print(time.strftime("%X"))
	
	time.sleep(45)
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
    
