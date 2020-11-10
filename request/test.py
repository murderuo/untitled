import requests
import json
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

# sonuc=requests.get('https://twitter.com/i/videos/tweet/1209143227405807617').text
#
# print(sonuc)

def get_guest_token():

    url='https://twitter.com/i/videos/tweet/1209143227405807617'
    browserpath=".\chromedriver.exe"  # this is win os path
    chromeOptions=webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    browser=webdriver.Chrome(executable_path=browserpath,options=chromeOptions)
    browser.get(url)
    time.sleep(2)
    page_code=browser.page_source
    soup=bs(page_code,"html.parser")
    blob_object=soup.find("video")
    blob=blob_object.get_attribute_list('src')
    blob_url_list=blob[0].replace('blob:','').split('/')
    print(blob_url_list)
    new_url='https://amp.twimg.com/v/'+blob_url_list[3]
    # print(new_url)
    r=requests.get(new_url)
    print(r.text)
    print(r)

    # time.sleep(20)





    # sesion=requests.Session()
    # response=sesion.get('https://twitter.com/i/videos/tweet/1209143227405807617')
    # print(response)
    # time.sleep(1)
    # sesion

    # url=requests.get('https://twitter.com/i/videos/tweet/1209143227405807617')
    #
    # print(url.text)
    # time.sleep(2)
    # video_player_response=requests.get('https://amp.twimg.com/v/f20a4174-eb4e-4a8c-a28a-3751e929d489')
    # print(video_player_response)
    # print(video_player_response)##video sayfasının html kodu

    # js_file_url=re.findall('src="(.*js)',video_player_response)[0]  ## https://abs.twimg.com/web-video-player/TwitterVideoPlayerIframe.1c7d5c71349918c3.js
    # js_file_response=requests.get(js_file_url).text
    # print(js_file_response) ## video dosyasındaki js içeriği
    # bearer_token_pattern=re.compile('Bearer ([a-zA-Z0-9%-])+')
    # bearer_token=bearer_token_pattern.search(js_file_response)
    # bearer_token=bearer_token.group(0)
    # print(bearer_token)
    #
    # res=requests.post("https://api.twitter.com/1.1/guest/activate.json")
    # print(res.text)
    # # res_json=json.loads(res.text)
    # # requests.headers.update({'x-guest-token':res_json.get('guest_token')})
    #
    #
    #
    # # res=requests.post("https://api.twitter.com/1.1/guest/activate.json")
    # res_json=json.loads(res.text)
    # sonuc2=requests.headers.update({'x-guest-token':res_json.get('guest_token')})
    # print(sonuc2)

get_guest_token()