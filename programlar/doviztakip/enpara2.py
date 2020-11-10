import requests
from bs4 import BeautifulSoup
import time
import locale


def enparacom():

    
    url= "https://www.qnbfinansbank.enpara.com/doviz-kur-bilgileri/doviz-altin-kurlari.aspx"

    r= requests.get(url)
    icerik=BeautifulSoup(r.content,"lxml")
   

    table=icerik.find("div",attrs={"id":"pnlContent"})
    #print(table)
    spans=table.find_all("span")
    for span in spans:
        dls=span.find_all("dl")
        for dl in dls:
            print(dl.dt.text,dl.dd.text,dl.dd.next_sibling.text)

enparacom()
