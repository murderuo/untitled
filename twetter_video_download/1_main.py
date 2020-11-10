import requests
import json
import time
import re

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


def __get_bearer_token():
    video_player_url=video_player_prefix+tweet_data['id']
    video_player_response=requests.get(video_player_url).text

    js_file_url=re.findall('src="(.*js)',video_player_response)[0]
    js_file_response=requests.get(js_file_url).text

    bearer_token_pattern=re.compile('Bearer ([a-zA-Z0-9%-])+')
    bearer_token=bearer_token_pattern.search(js_file_response)
    bearer_token=bearer_token.group(0)
    # this bellow token is extreme token idk what is it doing. if you want to use it, pls do comment rows up this rows
    # bearer_token="Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    req.headers.update({'Authorization':bearer_token})
    # __get_guest_token()
    # print(bearer_token)
    return bearer_token




def getvideo_url(tweet_url):
    tweet_data['tweet_url']=tweet_url.split('?',1)[0]
    tweet_data['user']=tweet_data['tweet_url'].split('/')[3]
    tweet_data['id']=tweet_data['tweet_url'].split('/')[5]
    token = __get_bearer_token()
    # guest_token=__get_guest_token()
    tweet_id = tweet_url.split("/")[5]
    hidir = {"Authorization":token}
    # guest_header={'x-guest-token':guest_token}
    s = requests.Session()
    s.headers.update(hidir)
    # s.headers.update(guest_header)
    json_link = "https://api.twitter.com/1.1/statuses/show/" + tweet_id + ".json?&tweet_mode=extended"
    resp = s.get(json_link).json()

    # print(resp)
    try:
        # url=resp["extended_entities"]["media"][0]["video_info"]["variants"][0]["url"] #this is one video file
        variants=resp["extended_entities"]["media"][0]["video_info"]["variants"]
        # print(variants)
        bitrate=0
        chosen_video=""
        for i in range(len(variants)):
            if variants[i]['content_type'] == "application/x-mpegURL": continue
            # print(variants[i])
            if variants[i]['bitrate'] > bitrate:
                bitrate=variants[i]['bitrate']
                chosen_video=variants[i]["url"]
        return chosen_video
    except :
        print("video url not found..trying other method. ")
        try:
            good_bearer_token="Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
            new_header={"Authorization":good_bearer_token}
            s.headers.update(new_header)
            json_link="https://api.twitter.com/1.1/statuses/show/"+tweet_id+".json?&tweet_mode=extended"
            resp2=s.get(json_link).json()
            variants=resp2["extended_entities"]["media"][0]["video_info"]["variants"]
            # print(variants)
            bitrate=0
            chosen_video=""
            for i in range(len(variants)):
                if variants[i]['content_type'] == "application/x-mpegURL": continue
                # print(variants[i])
                if variants[i]['bitrate'] > bitrate:
                    bitrate=variants[i]['bitrate']
                    chosen_video=variants[i]["url"]
            return chosen_video
        except:
            d={"url":tweet_url} #savetweetvid web adres submit form input value
            try:
                def other_way():
                    action_post=s.post('https://www.savetweetvid.com/tr/downloader',d)
                    # print(action_post.text)
                    time.sleep(2)
                    all_urls=re.findall('https://video[a-zA-Z0-9_.:/\?=-]*',action_post.text)
                    # print(all_urls)
                    uniq_urls=set(all_urls)
                    if '.mp4?tag' in list(uniq_urls)[0]: return list(uniq_urls)[0]
                    else: other_way()
                url=other_way()
                return url
            except:
                return 404


def save_video(video_url):
    if video_url==404: print("Video file doesnt save..")
    else:
        video_request=requests.get(video_url)
        if video_request.status_code == 200:
            with open('./video/'+video_url.split('/')[4]+'.mp4','wb') as f:
                f.write(video_request.content)
        print(f"video saved..{video_url}")

# tweet_url="https://twitter.com/XHTurkey/status/1232553400136609792"
# tweet_url="https://twitter.com/Cayistihbarattv/status/1232567069624930305"
# tweet_url="https://twitter.com/RealistBarmeN/status/1232654247629508608"
# tweet_url="https://twitter.com/bilimarsivi/status/1232659739483557888"
# tweet_url="https://twitter.com/tcbuyuksehir/status/1232722370479230978"
# tweet_url="https://twitter.com/SkyNews/status/1232915547198803968"
# tweet_url="https://twitter.com/meral_aksener/status/1232912077246881793"
# tweet_url="https://twitter.com/XHNews/status/1232931191747227649"
# tweet_url="https://twitter.com/sputnik_TR/status/1233011649994379264"
tweet_url="https://twitter.com/SkyNews/status/1233303812825395200"
tweet_url="https://twitter.com/SkyNewsWeather/status/1233297438150217728"
tweet_url="https://twitter.com/politikaloji/status/1233302378608197633"
video=getvideo_url(tweet_url)
# save_video(video)
print(video)
# from notify_run import Notify
# notify = Notify()
# notify.send(video)
