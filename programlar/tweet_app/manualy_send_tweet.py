import tweepy
import random
import time



consumer_key = "NETkPE2wIwbTcM7dh9GViUpc1"
consumer_secret = "WnldObFFxQW2RpGyhtOQYnBW9oHin0IK9AxKybr0lY8ssm14CM"
access_token = "70399566-feNknejcNjn7VV2PIGuFYgmdjSlpHrR3h7NscYeFz"
access_token_secret = "mxHaJ0JU1NlOrz0j8D6ah5zglnY2IqDCbNn0tWHSDygz8"

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)

api = tweepy.API(giris)
kullanici=api.get_user('asirihaklii')
print(type(kullanici))

print(kullanici.followers_count)



print(type(kullanici._json))


for k,v in kullanici._json.items():
	print(k,f'\t\t{v}')

#
# user_id=tweepy.API.user_timeline('asirihaklii')
# print(user_id)