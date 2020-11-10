import random




def kelimeyi_karistir(k):
    n=[",",".","?","!"]
    d_kelime=""

    d_kelime += k[0]
    kortasi = list(k[1:-2])
    random.shuffle(kortasi)
    for ortadakiharf in kortasi:
        d_kelime += ortadakiharf
    d_kelime += k[-2]+k[-1]

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
    d_kelime += klme3[-1]+klme3[-2]+klme3[-3]

    return d_kelime

k="kifayetsiz..."
test=kelimeyi_karistir3(k)

print(test)



# dkelime=""
#
# for h in kelime:
#     if h.index(h)==1:
#         dkelime+=h
#         continue
#     else:
#
#         dkelime+=random.choice()
#         if len(dkelime)==len(kelime):
#             break
#
#
# print(dkelime)
#
