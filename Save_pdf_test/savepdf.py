from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import  pdfkit

pdfkit.from_string('Hello!', 'out.pdf')


link = "https://www.google.com.tr"
#browserpath = "/usr/local/bin/chromedriver" #this is mac os path
browserpath = "..\Save_pdf_test\chromedriver.exe" #this is win os path
chromeOptions=webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")
browser = webdriver.Chrome(executable_path=browserpath,options=chromeOptions)
# browser=webdriver.Ie()
time.sleep(2)
browser.get(link)
source=browser.page_source
print(source)


time.sleep(3)
# print(browser.title)



browser.close()
