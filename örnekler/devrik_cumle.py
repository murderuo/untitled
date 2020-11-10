import random

cumle="sen, ben, biz. uzaklara gitsek, kimse bize karışmasa. Bağırsak çağırsak aleme... olmaz mı?"
yeni_c=""
d_cumle=[]
n=[",",".","?","!","...","'"]
kelimeler=cumle.split(" ")

def kelimeyi_karistir(klme):
    kortasi = []
    d_kelime=""
    d_kelime += klme[0]
    kortasi = list(klme[1:-2])
    random.shuffle(kortasi)
    for ortadakiharf in kortasi:
        d_kelime += ortadakiharf
    d_kelime += klme[-2]+klme[-1]
    return d_kelime

def kelimeyi_karistir2(klme2):
    d_kelime=""
    d_kelime += klme2[0]
    kortasi = list(klme2[1:-1])
    random.shuffle(kortasi)
    for ortadakiharf in kortasi:
        d_kelime += ortadakiharf
    d_kelime += klme2[-1]

    return d_kelime

def kelimeyi_karistir3(klme3):
    d_kelime=""
    d_kelime += klme3[0]
    kortasi = list(klme3[1:-3])
    random.shuffle(kortasi)
    for ortadakiharf in kortasi:
        d_kelime += ortadakiharf
    d_kelime += klme3[-4]+klme3[-1]+klme3[-2]+klme3[-3]

    return d_kelime




for k in kelimeler:
    if len(k)<=3 or (k[-1] in n and len(k)<=4):
        d_cumle.append(k)

    elif k[-1]+k[-2]+k[-3] in n:
        ucnokta = kelimeyi_karistir3(k)
        if ucnokta == k:
            ucnokta = kelimeyi_karistir3(k)
            d_cumle.append(ucnokta)
        else:
            d_cumle.append(ucnokta)

    elif len(k)>3 and k[-1] in n :
        d_kel=kelimeyi_karistir(k)
        if d_kel==k:
            d_kel = kelimeyi_karistir(k)
            d_cumle.append(d_kel)
        else:
            d_cumle.append(d_kel)
    elif len(k)>=4:
        nkelime=kelimeyi_karistir2(k)
        if nkelime==k:
            nkelime = kelimeyi_karistir2(k)
            d_cumle.append(nkelime)
        else:
            d_cumle.append(nkelime)

for kel in d_cumle:
    yeni_c+=kel+" "

print(yeni_c)
