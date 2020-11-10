from selenium import webdriver
import time
import requests



class TwitterCheck:
    def __init__(self):

        # self._link = "https://twitter.com/murderuo"
        self._link = "https://twitter.com/DijitalHabitat"
        #browserpath = "/usr/local/bin/chromedriver" #this is mac os path
        browserpath = ".\chromedriver.exe" #this is win os path
        # chromeOptions=webdriver.ChromeOptions()
        # chromeOptions.add_argument("--headless")
        # self.browser = webdriver.Chrome(executable_path=browserpath,options=chromeOptions)
        self.browser = webdriver.Chrome(executable_path=browserpath)



    def openSite(self,url="https://twitter.com/murderuo"):
        self._link=url
        self.browser.get(self._link)

    def wait(self,m):
        time.sleep(m)

    def findClassObjectText(self,class_name):
        my_bio=self.browser.find_element_by_xpath(class_name).text
        text=my_bio.text
        return text

    def findXpathObjectText(self,xpath_name):
        my_bio=self.browser.find_element_by_xpath(xpath_name)
        text=my_bio.text
        return text

    def findXpathObject(self,xpath_name):
        object=self.browser.find_element_by_xpath(xpath_name)
        return object

    def findXpathObjectClick(self,xpath_name):
        click_item=self.findXpathObject(xpath_name)
        click_item.click()

    def sendKeys(self,xpath_name,keys):
        send=self.findXpathObject(xpath_name)
        send.send_keys(keys)

    def saveScreenShot(self,fname):
        self.browser.save_screenshot(fname)



if __name__=="__main__":
    sertifikasiz_giris='//*[@id="form1"]/div[3]/div/div[1]/a'
    check=TwitterCheck()
    check.wait(2)
    check.openSite('https://www.e-icisleri.gov.tr/IBYetki/Login.aspx')
    check.wait(1)
    # value=check.findXpathObjectText('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p')
    # print(value)
    check.findXpathObjectClick(sertifikasiz_giris)
    check.wait(1)
    # k_adi='//*[@id="TextBoxKullaniciAd"]'
    # k_sifre='//*[@id="TextBoxParola"]'
    # check.sendKeys(k_adi,'ugur.okur@icisleri.gov.tr')
    # check.wait(1)
    # check.sendKeys(k_sifre,'ob478$93m')
    captcha='//*[@id="CaptchaLoginIslemleri_captchaImage"]'
    captcha_img=check.findXpathObject(captcha)
    # src=img.get_attribute('src')  #captcha url
    # print(src)
    # captcha_img.save_screenshot('captcha.png')
    check.saveScreenShot("captcha.jpg")




    # resource=urlopen(src)
    # output=open("file01.jpg","wb")
    # output.write(resource.read())
    # output.close()

    # img=requests.get(src)  # fetch image
    # with open('image.jfif','wb') as writer:  # open for writing in binary mode
    #     writer.write(img.read())
    #     writer.close()



