from googletrans import Translator

translator = Translator()

while 1:

    kelime=input("\nkelimeyi giriniz :")
    ulke= translator.detect("okul")
    try:

        if ulke.lang =='en':
            ceviri=translator.translate(kelime, dest='tr')
            # print(ceviri.extra_data.get('all-translations'))
            for i in ceviri.extra_data.get('all-translations'):
                for k in i[1]:
                    print(k, end=', ')
            # print(ceviri.text)

        elif ulke.lang=='tr':
            tr=translator.translate(kelime,dest='en')
            # print(tr.extra_data.get('all-translations'))
            for i in tr.extra_data.get('all-translations'):
                for k in i[1]:
                    print(k,end=', ')
                # print(i[1])
            # print(tr.extra_data)
        else:
            print("bir kelime giriniz,girilen kelime: %s" % kelime)
    except:
        print("Çevirisi yapılamadı")
