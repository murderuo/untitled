import requests
from bs4 import BeautifulSoup
import time
import locale
from itertools import product

def enparacom():

    
    url= "https://www.qnbfinansbank.enpara.com/doviz-kur-bilgileri/doviz-altin-kurlari.aspx"

    r= requests.get(url)
    icerik=BeautifulSoup(r.content,"lxml")
   

    table=icerik.find("div",attrs={"id":"pnlContent"})
    #print(table)
    cinsler=table.find_all("div",attrs={"class","dlContspan"})
    fiyatlar=table.find_all("div",attrs={"class","dlCont"})

    for i in range(-1,8):
        A=cinsler[i].text+" Alış(Bizim Satış)"
        B=cinsler[i+1].text+" Satış(Banka Satış)"

        afyt=fiyatlar[i].find("span").text
        sfyt=fiyatlar[i+1].find("span").text
        print(A,afyt)
        print(B,sfyt)


##    for cins in cinsler:
##        #cns=cins.find("div",attrs={"class","dlContspan"})
##        A=cins.text+" Alış(Bizim Satış)"
##        B=cins.text+" Satış(Banka Satış)"
##        print(A)
##        print(B)
##
##    fiyatlar=table.find_all("div",attrs={"class","dlCont"})
##    for fiyat in fiyatlar:
##        fyt=fiyat.find("span").text
##        print(fyt)

##    for cins,fiyat in product(cinsler,fiyatlar):
##    
##        A=cins.text
##        B=cins.text
##        print(A)
##        
##
##    
##    
##        fyt=fiyat.find("span").text
##        print(fyt)

enparacom()
