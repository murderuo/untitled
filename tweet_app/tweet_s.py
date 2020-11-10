import tweepy
import random
import	time



consumer_key = "dKy2I5WIl7hgcNtpipXIGnnce"
consumer_secret = "Mm9ViLSz4weJPsa8KZf264lj8ceYoz93eDGRe2Bs3n314NVpUd"
access_token = "70399566-PK9qHCRxbrUd4Y28wUcSG30gohTTv429KNpVSwrk0"
access_token_secret = "7G5oVCiJpsIZRaBWEzxnjhSPKtFHsobiDLFtNL3Fm33H1"

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)

api = tweepy.API(giris)

while 1:
        

	tweet_id=random.randint(1,10000)
	tag_id=random.randint(0,9)
	status=[
        'Seçime kadar #bedelliaskerlik meselesi çözülmelidir!Başbakanımızın da dediği gibi buradan elde edilen gelir memleketin yararına olacak kurumlara aktarılmalıdır.@Akparti @BA_Yildirim @dbdevletbahceli @RT_Erdogan @TC_Basbakan',
	'#BedelliAskerlik #MeclisteOlmalı gözardı yapılmamalı gündemden kaldırılmamali seçimden önce getirmeli ve bunca insana mağdur edilmemeli..',
	'Her kesimin sorunu çözüldü sıra #6MayısBedelliMüjdesi @RT @TC_Basbakan @nurettincanikli #BedelliAskerlik Gençler talep ediyor duyun sesimizi',
	'İki dudağının arasında milyonlarca gencin umudu, hayatı, huzuru var Reis #BedelliAskerlik sözünü tut artık @RT_Erdogan @Akparti Binlerce genç milyonlarca aile ferdi #BedelliAskerlik umuduyla bekliyor @dbdevletbahceli #6MayıstaBedelliMüjdesi',
	'#6MayısBedelliMüjdesi verilmeli sorunun cozumu iki dudaginizin arasinda cikacak iki kelimeye bagli #BedelliAskerlik @RT_Erdogan @dbdevletbahceli @Akparti @MHP_Bilgi',
	'#6MayıstaBedelliMüjdesi Sayın Cumhurbaşkanımız @RT_Erdogan "Daha Öncede #BedelliAskerlik Yasasını Uyguladık ve Terörle Mücadelede Zaafiyet Oluşturmadı, Gelinen Noktada Bu Yasanın Tekrar Uygulanması Zaruri Olmuştur" @dbdevletbahceli',
	'#bedelliaskerlik bu konun kanayan yara gibi devam etmesine artik dur demenizi istiyoruz.GENÇLERE Güven huzur ve kafasında sorun olmadan yollarına devam etmesine olanak veriniz.saygilar. #DevletBahceli #BasbakanYıldırım #receptayyiperdogan #BedelliAskerlikGeliyor'
        ]
	tags=['#yas25bedel15',
              '#BedelliAskerlik',
              '#BedelliAskerlikGeliyor',
              '#6MayıstaBedelliMüjdesi',
              '@RT_Erdogan',
              '@TC_Basbakan',
              '@mahirunal',
              '#BedelliAskerlikGeliyor',
              '#6MayisBedelliMüjdesi',
              '#BahcelidenBedelliMujdesi']


	if tweet_id<1500:
		print(tweet_id)
		api.update_status(status[0]+" "+ str(tweet_id))

	elif tweet_id>1500 and  tweet_id<2500:
		print(tweet_id)

		api.update_status(status[1]+" "+ str(tweet_id))
	elif tweet_id>2500 and tweet_id<3500:

		print(tweet_id)
		api.update_status(status[2]+" "+ str(tweet_id))
		
	elif tweet_id>3500 and tweet_id <5500:
		
		print(tweet_id)
		api.update_status(status[3]+" "+ str(tweet_id))
		
	elif tweet_id>5500 and tweet_id <7500:
		print(tweet_id)
		api.update_status(status[4]+" "+ str(tweet_id))
		
	elif tweet_id>7500 and tweet_id <8500:
		print(tweet_id)
		api.update_status(status[5]+" "+ str(tweet_id))

	elif tweet_id>8500 and tweet_id <9000:
		print(tweet_id)
		api.update_status(status[6]+" "+ str(tweet_id))
	
	elif tweet_id>9000  and tweet_id<10000:
	
		print(tweet_id)
                api.update_status( status[6]+" "+tags[tag_id] )

    time.sleep(70)

print(tweet_id)		

#api.update_status(status="Python Amca #pyamca")

#twitler = api.home_timeline()
#for twit in twitler:
#    print (twit.text)
#    print ("**")





