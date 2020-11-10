import urllib.request
search_phrase = 'crypto'
with urllib.request.urlopen('https://twitter.com/i/status/1209076184744701952') as response:
   html = response.read().decode("utf8") # convert to string
   # first_pos = html.find(search_phrase)
   # print(html[first_pos-10:first_pos+10])
   print(html)