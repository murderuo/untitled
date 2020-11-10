import requests
from bs4 import BeautifulSoup
import time



url= "http://www.doviz.com"

# kitap=input("aranacak kitabı giriniz:")
# kelime=""
# for h in kitap:
# 	if (h==" "):
# 		h="%20"
# 	kelime+=h

# url+=kelime
r= requests.get(url)
icerik=BeautifulSoup(r.content,"lxml")
icerik.prettify()


table=icerik.find_all("div",attrs={"class":"header-row"})
print(table)
item=table.select("ul > li")
# item=table.find_all("ul")
print (item)


# miktarlarUL=miktarlar.find_all("ul")
# print(miktarlar)
# print(str(miktarlarUL))

# for ss in sayfaSayisiUL:
#        print (ss)


# sayi=total.text.split(" ")
# kayit_sayisi=int(sayi[0])
# ss=kayit_sayisi//42+1

# if ss>1 :
   
               
#    print("########## SAYFA SAYISI:  ",ss-1,"kayıt sayısı: ",kayit_sayisi)
#    for i in range(1,ss):
               
#        url2=url+'&cat=0%2C10001&parentId=10001#/page='+str(i)+'/sort=relevance,desc/categoryid=0,10001/parentId=10001/lg=undefined/price=-1,-1/ldir=h'
# ##        time.sleep(1)
#        rq=requests.get(url2)
       
#        icerik=BeautifulSoup(rq.content,"lxml")
#        time.sleep(2)       

#        kitaps=icerik.find_all("div",attrs={"class":"list-cell"})
#        print("#####URL#### : ",url2)

#        for kitap in kitaps:
               
#                kitap_adi=kitap.find("div",attrs={"class":"details"}).h3.text
#                fiyati=kitap.find("span",attrs={"class":"price"}).text

               
#                print("Kitap adi: ",kitap_adi,"\t\t\tFiyatı :",fiyati)
#        print("########",i," .sayfa sonu########################")
#        url2=""
# else:
       
#        rq=requests.get(url)
       
#        icerik=BeautifulSoup(rq.content,"lxml")
              

#        kitaps=icerik.find_all("div",attrs={"class":"list-cell"})
#        print("#####URL#### : ",url)

#        for kitap in kitaps:
#                kitap_adi=kitap.find("div",attrs={"class":"details"}).h3.text
#                fiyati=kitap.find("span",attrs={"class":"price"}).text

               
#                print("Kitap adi: ",kitap_adi,"\t\t\tFiyatı :",fiyati)

