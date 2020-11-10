bitrate=0
chosen_video=""
variants=[{'bitrate': 1280000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/ext_tw_video/1232659699646025728/pu/vid/540x540/zrebBoM8JGN8gtDa.mp4?tag=10'}, {'bitrate': 832000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/ext_tw_video/1232659699646025728/pu/vid/480x480/K4aanoxpJ8i7n1HO.mp4?tag=10'}, {'bitrate': 432000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/ext_tw_video/1232659699646025728/pu/vid/320x320/GWhdsmlx4x7u52Da.mp4?tag=10'}, {'content_type': 'application/x-mpegURL', 'url': 'https://video.twimg.com/ext_tw_video/1232659699646025728/pu/pl/Ba9SBrhgoINh_mhX.m3u8?tag=10'}]
for i in range(len(variants)):
    if variants[i]['content_type']=="application/x-mpegURL":
        continue
    # print(variants[i])
    if variants[i]['bitrate']>bitrate:
        bitrate=variants[i]['bitrate']
        chosen_video=variants[i]["url"]



print(bitrate,chosen_video)




# for i in variants:
#     print(i['url'])