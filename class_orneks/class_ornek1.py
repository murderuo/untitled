sesli_harfler = 'aeıioöuü'
sayaç = 0
kelime = input('Bir kelime girin: ')

def seslidir(harf):
    print('sayaç değişkeninin değeri şu anda: ', sayaç)
    return harf in sesli_harfler

def artır():
    global sayaç
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır()))