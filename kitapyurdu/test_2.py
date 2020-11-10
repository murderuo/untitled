import requests
from bs4 import BeautifulSoup

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


    for kitap in kitaps:
        print(kitap.span.text)
        print(kitap.find("div",attrs={"class":"price-new"}).text)
except:
    print("kitap bulunamadı")

    



