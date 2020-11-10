import requests
from bs4 import BeautifulSoup

url= "http://www.kitapyurdu.com/index.php?route=product/search&filter_name="

kitap=input("aranacak kitabı giriniz:")
kelime=""
for h in kitap:
    if (h==" "):
        h="+"
    kelime+=h
    
url+=kelime

r= requests.get(url)

icerik=BeautifulSoup(r.content,"lxml")
kitaps=icerik.find("ul",attrs={"class":"product-grid small jcarousel-skin-opencart"})

#kitaps=kitaps.find_all("li")
kitaps=kitaps.find_all("div",attrs={"class":"name ellipsis"})
#kitaps=kitaps.find_all("span")
for kitap in kitaps:
    print(kitap.span.text)
    

#s=r.status_code

##print(url,"\n")
##
##print(kelime,"\n")

##print(kitap,"\n")




