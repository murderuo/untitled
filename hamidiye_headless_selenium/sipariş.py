from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



link = "https://siparis.hamidiye.istanbul/giris.php"
#browserpath = "/usr/local/bin/chromedriver" #this is mac os path
browserpath = ".\chromedriver.exe" #this is win os path
chromeOptions=webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")
browser = webdriver.Chrome(executable_path=browserpath,options=chromeOptions)
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





login(link)

time.sleep(2)
sip_ver=browser.find_element_by_xpath("/html/body/div/div[2]/ul/li[2]/a")
sip_ver.click()
time.sleep(2)
urun_list=browser.find_element_by_css_selector(".siparis").click()
time.sleep(1)
damacana_select=browser.find_element_by_xpath("//li[text() = '19 lt. DAMACANA SU 11 TL (Depozito 15 TL)--- YABANCI DAMACANA DEĞİŞİM BEDELİ 5 TL İSTANBUL İÇİ EVE TESLİM FİYATLARIMIZDIR']").click();
time.sleep(1)
mesaj=browser.find_element_by_xpath('//*[@id="textarea2"]')
mesaj.click()
time.sleep(1)
sip_buton=browser.find_element_by_xpath('//*[@id="basicform"]/form/p[4]/button').click()


print("Sipariş verildi.")
time.sleep(3)
browser.close()
