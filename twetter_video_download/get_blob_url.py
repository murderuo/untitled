## Dependencies
from bs4 import BeautifulSoup as bs
import re
## Data
page_code = """"C:\Program Files\Python36\python.exe" "C:/Users/ugurokur/Desktop/kişisel bilgilerim/python_uygulama/PythonRep/programlar/request/test.py"
<html><head><style id="react-native-stylesheet"></style>
  <style>
    body, html {
      margin: 0;
      padding: 0;
    }

    #video {
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
    }
  </style>
<script type="text/javascript" charset="utf-8" async="" src="https://abs.twimg.com/web-video-player/ondemand.PlayerHls12.f25df597b580e9ae.js"></script></head>
<body>
  <div id="video"><div style="cursor: pointer; height: 100%; width: 100%; position: relative; color: rgba(255, 255, 255, 0.85); font-size: 13px; font-weight: 400; font-family: &quot;helvetica neue&quot;, arial; line-height: normal; transform: translateZ(0px);"><div role="button" tabindex="0" style="position: absolute; height: 100%; width: 100%;"><div style="height: 100%; position: relative; transform: translateZ(0px); width: 100%;"><div style="height: 100%; position: absolute; width: 100%;"><div style="position: relative; width: 100%; height: 100%; background-color: transparent; overflow: hidden;">
  <video preload="none" playsinline="" poster="https://pbs.twimg.com/ext_tw_video_thumb/1209142959473676289/pu/img/1tCtKeBOEhD9FCIH.jpg" 
  src="blob:https://twitter.com/503e40cc-790d-4725-a4fa-0649b7d93acd" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video></div></div></div></div><div><div role="button" data-focusable="true" tabindex="0" class="css-18t94o4 css-1dbjc4n r-1awozwy r-vvn4in r-4gszlv r-1krgy4v r-1loqt21 r-1777fci r-1bboaxi r-u8s1d r-rzrk0s r-1sc8clx" data-testid="poster" style="background-image: url(&quot;https://pbs.twimg.com/ext_tw_video_thumb/1209142959473676289/pu/img/1tCtKeBOEhD9FCIH.jpg&quot;);"><div data-testid="posterPlayBtn"><div aria-haspopup="false" aria-label="Play" role="button" data-focusable="true" tabindex="0" class="css-18t94o4 css-1dbjc4n r-urgr8i r-11mg6pl r-sdzlij r-1phboty r-14f9gny r-e6wyp1 r-o7ynqc r-6416eg r-1p15a4t"><div class="css-1dbjc4n r-1awozwy r-1pi2tsx r-1777fci r-u8s1d r-13qz1uu"><svg viewBox="0 0 24 24" class="r-jwli3a r-4qtqp9 r-yyyyoo r-1sa8knb r-dnmrzs r-1dsia8u r-bnwqim r-1plcrui r-lrvibr r-gcko2u"><g><path d="M20.436 11.37L5.904 2.116c-.23-.147-.523-.158-.762-.024-.24.132-.39.384-.39.657v18.5c0 .273.15.525.39.657.112.063.236.093.36.093.14 0 .28-.04.402-.117l14.53-9.248c.218-.138.35-.376.35-.633 0-.256-.132-.495-.348-.633z"></path></g></svg></div></div></div></div><div class="css-1dbjc4n r-1nlw0im r-1r74h94 r-u8s1d"><span style="opacity: 1; transition: opacity 0.15s ease-in-out 0s;"><div class="css-1dbjc4n r-18u37iz"><div class="css-1dbjc4n r-1ifrmw8"><div class="css-1dbjc4n r-1awozwy r-1810x6o r-re1h2s r-1as3g83 r-7q8q6z r-z80fyv r-1777fci r-ou255f"><div dir="auto" class="css-901oao r-jwli3a r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-q4m81j r-qvutc0"><span data-testid="duration" dir="auto" class="css-901oao css-16my406">0:51</span></div></div></div><div class="css-1dbjc4n"><div class="css-1dbjc4n r-1awozwy r-1810x6o r-qpmf2f r-dfv94e r-7q8q6z r-z80fyv r-1777fci r-ou255f"><div dir="auto" class="css-901oao r-jwli3a r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-q4m81j r-qvutc0"><span data-testid="viewCount" dir="auto" class="css-901oao css-16my406 r-lrvibr" style="color: inherit;"><span>44,6&nbsp;B görüntülenme</span></span></div></div></div></div></span></div><div class="css-1dbjc4n r-1nlw0im r-u8s1d r-3mc0re"><span style="opacity: 1; transition: opacity 0.15s ease-in-out 0s;"></span></div></div></div></div>
    <script src="https://abs.twimg.com/web-video-player/TwitterVideoPlayerIframe.1c7d5c71349918c3.js"></script><style>@keyframes TwitterVideoPlayerBufferingAnimation { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>



</body></html>

Process finished with exit code 0
"""
# text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"
## One-Liner
soup=bs(page_code,"html.parser")
blob_object=soup.find("video")
blob=blob_object.get_attribute_list('src')
print(blob[0].replace('blob:',''))
# print(blob_object)
