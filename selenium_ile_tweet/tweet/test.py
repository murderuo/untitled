from selenium import webdriver
import time	


browser = webdriver.Chrome()
browser.get('https://twitter.com/')

time.sleep(10)


input_id=browser.find_element_by_name("session[username_or_email]")
input_pw=browser.find_element_by_name("session[password]")

input_id.send_keys("murderuo")
input_pw.send_keys("375201.Ugur")

lg_bt=browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[1]/form/input[1]")
lg_bt.click()

time.sleep(5)
