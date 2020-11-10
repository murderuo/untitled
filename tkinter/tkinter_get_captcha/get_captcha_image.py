from selenium import webdriver
import time
from PIL import Image
from PIL import ImageTk
from tkinter import *

# driver=webdriver.Chrome('chromedriver.exe')
# url="https://www.e-icisleri.gov.tr/IBYetki/Login.aspx"
# driver.get(url)
# time.sleep(2)
# sertifikasiz_giris='//*[@id="form1"]/div[3]/div/div[1]/a'
# driver.find_element_by_xpath(sertifikasiz_giris).click()
# time.sleep(1)
# # driver.find_element_by_xpath('//*[@id="CaptchaLoginIslemleri_captchaImage"]')
# driver.save_screenshot("captcha.png")


def resimKirp(resim_adi):
    img = Image.open(resim_adi)
    aa = (55, 480, 350, 550)
    crop_img = img.crop(aa)
    # dialog = Dialog.
    crop_img.load()
    crop_img.save("cropped.png")


# def resimGoster():
#     root=Tk()
#     canv=Canvas(root,width=250,height=60,bg='white')
#     canv.grid(row=2,column=3)
#
#     img=ImageTk.PhotoImage(Image.open(".\s_captcha.jpg"))  # PIL solution
#     canv.create_image(0,0,anchor=NW,image=img)
#     root.mainloop()


# time.sleep(2)
resimKirp("captcha.png")
# time.sleep(2)
# resimGoster()