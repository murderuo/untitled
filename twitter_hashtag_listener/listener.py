import tweepy
#override tweepy.StreamListener to add logic to on_status

consumer_key="osUlOXxtORRiLQd2iNtQgPifH"
consumer_secret="TULYCcd9b5L678W6OBfXEy7cM3ErtJL6XxQDzMQKDOzOA6ITrt"

access_token="70399566-GcJfQqr3VLOuwRuG8yPSFxr44znKJieNl2ASasUUr"
access_token_secret="K7LlXPCaV2rsbJdJwb7gDw0BUfx8SUn2NluNsGX6G36SP"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text+"\n")



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['#bedelliaskerlik'], async=True)