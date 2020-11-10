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
    for oneLi in li:
            
        link=oneLi.find("a")
        baslik=link.find("span",attrs={"class":"menu-row1"}).text
        fiyat=link.find("span",attrs={"class":"menu-row2"}).text
        degisim=link.find("span",attrs={"class":"menu-row3"}).text
        print(baslik,fiyat,degisim,sep="\t")
        item+=1
        if item ==4:
            break

dovizcom()