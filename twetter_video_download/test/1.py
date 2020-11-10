import requests
import json
import time
import urllib.parse
import m3u8
from pathlib import Path
import re
import ffmpeg
import shutil

video_player_prefix = 'https://twitter.com/i/videos/tweet/'
video_api = 'https://api.twitter.com/1.1/videos/tweet/config/'
tweet_data = {}
req = requests.Session()

def __get_guest_token():
    res=req.post("https://api.twitter.com/1.1/guest/activate.json")
    res_json=json.loads(res.text)
    req.headers.update({'x-guest-token':res_json.get('guest_token')})
    guest_tok=res_json.get('guest_token')
    # print(guest_tok)
    return guest_tok


def __get_bearer_token(tweet_u):
    # video_player_url=video_player_prefix+tweet_data['id']
    # video_player_response=requests.get(video_player_url).text
    response=requests.get(tweet_u)
    print(response.text)
    # js_file_urls=re.findall('src="(.*js)',response.text)
    # print(js_file_urls)
    # js_file_response=requests.get(js_file_url).text

    bearer_token_pattern=re.compile('Bearer ([a-zA-Z0-9%-])+')
    bearer_token=bearer_token_pattern.search(js_file_response)
    bearer_token=bearer_token.group(0)
    req.headers.update({'Authorization':bearer_token})
    # __get_guest_token()
    print(bearer_token)
    return bearer_token


def getvideo_url(tweet_url):
    tweet_data['tweet_url']=tweet_url.split('?',1)[0]
    tweet_data['user']=tweet_data['tweet_url'].split('/')[3]
    tweet_data['id']=tweet_data['tweet_url'].split('/')[5]
    token = __get_bearer_token(tweet_url)
    guest_token=__get_guest_token()
    tweet_id = tweet_url.split("/")[5]
    hidir = {"Authorization":token}
    guest_header={'x-guest-token':guest_token}
    s = requests.Session()
    s.headers.update(hidir)
    s.headers.update(guest_header)
    json_link = "https://api.twitter.com/1.1/statuses/show/" + tweet_id + ".json"
    resp = s.get(json_link).json()
    # print(resp)
    try:
        url=resp["extended_entities"]["media"][0]["video_info"]["variants"][0]["url"]
        if '.m3u8' in url:
            print(url)
            return resp["extended_entities"]["media"][0]["video_info"]["variants"][1]["url"]
        else:
            return url
    except :
        print("video url not found..")
        print("trying other..")
        other_json="https://api.twitter.com/2/timeline/conversation/"+tweet_id+".json"
        resp2=s.get(other_json).json()
        n_token=__get_bearer_token()
        print(n_token)







        # print(resp2)
        # d={"url":tweet_url}
        # action_post=s.post('https://www.savetweetvid.com/tr/downloader',d)
        # time.sleep(1)
        # all_urls=re.findall('https://video[a-zA-Z0-9_.:/\?=]*',action_post.text)
        # uniq_urls=set(all_urls)
        # # print(list(uniq_urls))
        # return list(uniq_urls)[0]


def save_video(video_url):
    if video_url==404: print("Video file doesnt save..")
    else:
        video_request=requests.get(video_url)
        if video_request.status_code == 200:
            with open('./video/'+video_url.split('/')[4]+'.mp4','wb') as f:
                f.write(video_request.content)
        print(f"video saved..{video_url}")

# tweet_url="https://twitter.com/XHTurkey/status/1232553400136609792"
tweet_url="https://twitter.com/Cayistihbarattv/status/1232567069624930305"
video=getvideo_url(tweet_url)
save_video(video)