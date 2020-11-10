# twint-utils
These are utilizations of Twint. Please check out our collaboration guidelines to contribute to these.

## Mutuals Detector
Mufos.py uses Twint to detect a given seed accounts mutual followers. It can be incorporated into other more elaborate pipelines for social networks or millieu detection. It is too slow to be useful right now for accounts with massive follower/Following. Here is a [hosted version](https://colab.research.google.com/drive/1AOXQxkOWbq7KEHWVBRiOrYhTOSg3QTqq) that you can open in playground mode to play with.

## Media Downloader
accepts twint.output.tweets_list as an argument. 
```python
from twint_utils.tweets import media_downloader

tweets = twint.output.tweets_list                              
location = "./"
media_downloader.download_photos(get_tweets(tweets), location)
media_downloader.download_videos(get_tweets(tweets), location)
```

## Link Counter (link_counter.py)
This code takes a list of twitter usernames, iterates over them to find tweets where they shared links, and then sums up the base URLs of everyones links combined and turns it into a matplotlib bar graph. Please check code documentation for usage guidance. The code does take a bit to run depending on your tweet limit and how many accounts you pull.  Non-coder friendly hosted version [here](https://colab.research.google.com/drive/1AGgt2Qm2LThNAKeBsnbKRXgWgPc9kFN9).

## Related Hashtags Detector (related_hashtags.py)
This notebook finds other hashtags that are most commonly found with a given hashtag and creates a bar graph of them. This can be used to track how disinformation campaigns or stories are happening. Non-coder friendly hosted version [here](https://colab.research.google.com/drive/1dNSxohTBgNox0IiaGwqv66eFyxKBABHx).
