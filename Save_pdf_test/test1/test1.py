from selenium import webdriver
browserpath = "..\\test1\chromedriver.exe" #this is win os path

driver = webdriver.Chrome(executable_path=browserpath)
driver.get("https://www.google.co.uk");

# open new file
file = open(r"captures.html", "w")
file.write("<!DOCTYPE html><html><head></head><body width=\"600px\">")

# write image
file.write("<img src=\"data:image/png;base64,")
file.write(driver.get_screenshot_as_base64())
file.write("\">")

# close file
file.write("</body></html>")
file.close()

driver.quit()