from selenium import webdriver
from bs4 import BeautifulSoup as bs
from PIL import Image,ImageTk
import time
from captcha_dialog import ShowCaptcha
# from tkinter import *
# from main_window import Evrak

# driver=webdriver.Chrome('chromedriver.exe')
# url="https://www.e-icisleri.gov.tr/IBYetki/Login.aspx"


class IcısleriLogın:

    def __init__(self):
        self._captha_keys=""
        # self._link = "https://twitter.com/murderuo"
        self._link = "https://twitter.com/DijitalHabitat"
        #browserpath = "/usr/local/bin/chromedriver" #this is mac os path
        browserpath = ".\chromedriver.exe" #this is win os path
        chromeOptions=webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(executable_path=browserpath,options=chromeOptions)
        # self.browser = webdriver.Chrome(executable_path=browserpath)



    def openSite(self,url="https://twitter.com/murderuo"):
        self._link=url
        self.browser.get(url)

    def wait(self,m):
        time.sleep(m)

    def findClassObjectClick(self,class_name):
        class_item=self.browser.find_element_by_class_name(class_name)
        class_item.click()


    def findClassObjectText(self,class_name):
        my_bio=self.browser.find_element_by_xpath(class_name).text
        text=my_bio.text
        return text

    def findXpathObjectText(self,xpath_name):
        object_text=self.browser.find_element_by_xpath(xpath_name)
        return object_text.text

    def findXpathObject(self,xpath_name):
        object=self.browser.find_element_by_xpath(xpath_name)
        return object

    def findXpathObjectClick(self,xpath_name):
        click_item=self.findXpathObject(xpath_name)
        click_item.click()

    def sendKeys(self,xpath_name,keys):
        send=self.findXpathObject(xpath_name)
        send.send_keys(keys)


    def getCaptcha(self):
        # driver.get(url)
        # time.sleep(2)
        # sertifikasiz_giris='//*[@id="form1"]/div[3]/div/div[1]/a'
        # driver.find_element_by_xpath(sertifikasiz_giris).click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="CaptchaLoginIslemleri_captchaImage"]')
        self.browser.save_screenshot(".\\tmp\captcha.png")  # time.sleep(1)

    def cropCaptcha(self,resim_adi):
        img=Image.open(resim_adi)
        # aa=(55,480,350,550) #normal browser size
        aa=(62,210,280,265) #headless size
        crop_img=img.crop(aa)
        crop_img.load()
        crop_img.save(".\\tmp\cropped.png")  # time.sleep(1)

    def showCaptcha(self):
        self.dialog=ShowCaptcha()
        self._captha_keys=self.dialog.getValue()

    def inputCaptcha(self):
        while 1:
            if self._captha_keys=="":
                continue
            else:
                self.browser.find_element_by_xpath('//*[@id="CaptchaLoginIslemleri_tbCaptchaText"]').send_keys(self._captha_keys)
                time.sleep(1)
                self.browser.find_element_by_xpath('//*[@id="ButtonSifreliGiris"]').click()
                break

    def browserEnterKey(self):
        self.browser.switch_to.alert.accept()

    def getPageSourceCode(self):
        source=self.browser.page_source
        # html_source=bs(source,'html.parser')
        # return html_source
        return source

    def getHMTLSourceCode(self):
        source=self.browser.page_source
        # print(source)
        html_source=bs(source,'html.parser')
        all_ul=html_source.find_all('span',class_="rpText")
        if len(all_ul)>=18:
            counter_values = all_ul[1].get_text(), all_ul[2].get_text(), all_ul[16].get_text(), all_ul[14].get_text(), \
                             all_ul[15].get_text(), all_ul[19].get_text()
            if len(counter_values)!=6:
                time.sleep(10)
                self.clickEvrakPage()
                self.getHMTLSourceCode()
            else:
                return counter_values
        else:
            time.sleep(10)
            self.clickEvrakPage()
            self.getHMTLSourceCode()

    def birimKontrol(self):
        aktif_birim=self.findXpathObjectText('//*[@id="ctl00_ctl00_LabelAktifBirim"]')
        # print(aktif_birim)
        if aktif_birim=="İstanbul Valiliği":
            # print("Aktif birim {}.Birim değiştiriliyor..".format(aktif_birim))
            self.findClassObjectClick('AlternatifMenu')
            self.wait(2)
            self.findClassObjectClick('SolMenuYetki')
            self.wait(2)
            self.findXpathObjectClick('//*[@id="ctl00_ctl00_MessageBox1_ButtonTamam"]')

    def clickEvrakPage(self):
        self.findXpathObjectClick('//*[@id="ctl00_ctl00_ImageEvrak"]')
        self.wait(1)

    def gitEvrakPage(self):
        url='https://www.e-icisleri.gov.tr/Evrak/EvrakAnaSayfa/EvrakAnaSayfa.aspx'
        self.openSite(url)
        self.wait(2)

    def gitPostalanacakPage(self):
        url='https://www.e-icisleri.gov.tr/Evrak/Posta/PostalanmayiBekleyen.aspx'
        self.openSite(url)
        self.wait(2)


if __name__=="__main__":
    check=IcısleriLogın()


    sertifikasiz_giris='//*[@id="form1"]/div[3]/div/div[1]/a'
    check.wait(2)
    check.openSite('https://www.e-icisleri.gov.tr/IBYetki/Login.aspx')
    check.wait(1)
    # value=check.findXpathObjectText('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p')
    # print(value)
    check.findXpathObjectClick(sertifikasiz_giris)
    k_adi='//*[@id="TextBoxKullaniciAd"]'
    k_sifre='//*[@id="TextBoxParola"]'
    check.sendKeys(k_adi,'ugur.okur@icisleri.gov.tr')
    check.wait(1)
    check.sendKeys(k_sifre,'de273-mtv')
    check.getCaptcha()
    check.wait(1)
    check.cropCaptcha(".\\tmp\captcha.png")
    check.wait(1)
    check.showCaptcha()
###inputing##
    check.inputCaptcha()
    check.findXpathObjectClick('//*[@id="ButtonGerekce"]')
    check.wait(1)
    check.findXpathObjectClick('//*[@id="PanelGerekce"]/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/span/label')
    check.wait(1)
    check.findXpathObjectClick('//*[@id="ctl08_ButonGerekceliSifreliGiris"]')
    check.wait(1)
    check.browserEnterKey()
    check.wait(1)
    # exit()
##check brim kontrol##
    check.birimKontrol()
    check.wait(1)

##start get value###
    check.clickEvrakPage()
    # new_counts=tuple()
    counts=check.getHMTLSourceCode()
    print(counts)














