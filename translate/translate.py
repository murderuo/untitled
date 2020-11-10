from googletrans import Translator

translator = Translator()

while 1:

    kelime=input("\nkelimeyi giriniz :")
    ulke= translator.detect(kelime)
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

# print(ulke)


'''kullanımlar

>>> translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
>>> for translation in translations:
...    print(translation.origin, ' -> ', translation.text)
# The quick brown fox  ->  빠른 갈색 여우
# jumps over  ->  이상 점프
# the lazy dog  ->  게으른 개

dil tespiti:
>>> from googletrans import Translator
>>> translator = Translator()
>>> translator.detect('이 문장은 한글로 쓰여졌습니다.')
# <Detected lang=ko confidence=0.27041003>

'''
