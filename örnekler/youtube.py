import pafy
import vlc

url = "https://www.youtube.com/watch?v=vAKtNV8KcWg"
video = pafy.new(url)
best = video.getbest(preftype="webm")
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()


