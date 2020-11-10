import requests
from bs4 import BeautifulSoup

def kitapYurdu():

    url= "http://www.kitapyurdu.com/index.php?route=product/search&filter_name="

    kitap=input("aranacak kitabı giriniz:")
    kelime=""
    for h in kitap:
        if (h==" "):
            h="%20"
        kelime+=h
        
    url+=kelime
    try:
        r= requests.get(url)
    except:
        print("bağlantı kurulamadı...")
    try:
        icerik=BeautifulSoup(r.content,"lxml")
        kitaps=icerik.find("ul",attrs={"class":"product-grid small jcarousel-skin-opencart"})
        kitaps=kitaps.find_all("li")

        print("############# KİTAPYURDU SİTESİNDEN ARANIYOR #############")
        for kitap in kitaps:
            
            print(kitap.span.text)
            print(kitap.find("div",attrs={"class":"price-new"}).text)
    except:
        print("kitap bulunamadı")

    
def dR():

    url= "http://www.dr.com.tr/search?q="

    kitap=input("aranacak kitabı giriniz:")
    kelime=""
    for h in kitap:
        if (h==" "):
            h="%20"
        kelime+=h
        
    url+=kelime
    try:
        r= requests.get(url)
    except:
        print("bağlantı kurulamadı...")
    try:
        icerik=BeautifulSoup(r.content,"lxml")
        kitaps=icerik.find("div",attrs={"class":"list-cell"})
        #kitaps=kitaps.find_all("li")

        print("############# d&r SİTESİNDEN ARANIYOR #############")
        for kitap in kitaps:
            
            print(kitap.h3.text,kitap.find("span",attrs={"class":"price"}).text)
##            print()
    except:
        print("kitap bulunamadı")


kitapYurdu()

##dR()
