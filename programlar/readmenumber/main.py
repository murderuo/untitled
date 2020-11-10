readings=["one","two","three","four","five","six","seven","eight","nine","ten","ty",
          "eleven","twelve","thir","teen","fif","twenty","for","hundered"]

readings_dict={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight",
               "9":"nine","10":"ten","11":"eleven","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen",
               "16":"sixteen","17":"seventeen","18":"eighteen","19":"nineteeen"}
readings_dict2={"2":"twenty","3":"thirty","4":"forty","5":"fifty",
                "6":"sixty","7":"seventy","8":"eighty","9":"ninety"}

# def onlar(sayi):
#     sayi=sayi-basamakBul(sayi)*100
#     ob=basamakBul(sayi)
#     return ob

def basamakBul(sayi,before=""):
    read=""
    # if sayi==0:
    #     print(before)
    if (sayi >= 1) and (sayi < 20):
        read=before+" "+readings_dict[str(sayi)]
        print(read)
    if sayi>=20 and sayi<100:
        ob=int(sayi/10)
        bb=sayi%10
        if bb==0:
            read+=before+" "+readings_dict2[str(ob)]
            print(read)
        else:
            read+=before+" "+readings_dict2[str(ob)]+" "+readings_dict[str(bb)]
            print(read)
    if sayi>=100:
        yb=int(sayi/100)
        ob=sayi%100
        read+=readings_dict[str(yb)]+" hundred"
        print(ob)
        # read+=readings_dict[str(ob)]
        # if ob!=0 and (ob>=1) and (ob<20):
        # print(read)
        basamakBul(ob,read)

    # print(read)


while 1:
    try:
        sayi=int(input("1-999 aralığında bir sayı giriniz:"))
    except:
        print("Lütfen geçerli bir karakter giriniz")
    else:
        if sayi==0:
            print("Sıfırdan farklı bir sayı giriniz")
            continue
        if sayi>999:
            print("Lütfen Belirtilen aralıkta sayı giriniz")
            continue

    basamakBul(sayi)























# def yuzlerBasamak(sayi):
#     y_bas=int(sayi/10)
#     if y_bas>=10: y_bas=yuzlerBasamak(y_bas)
#     onlarBasamak(sayi-yuzlerBasamak(sayi)*100)
#     return y_bas
#
# def onlarBasamak(sayi):
#     sayi=sayi-yuzlerBasamak(sayi)*100
#     ob=yuzlerBasamak(sayi)
#     return ob
#
# def birlerbasamak(sayi):
#     sayi=sayi-(yuzlerBasamak(sayi)*100+onlarBasamak(sayi)*10)
#     return sayi

#
# while 1:
#     read=""
#     sayi=int(input("bir sayı giriniz:"))
#     if(sayi>=1) and (sayi<20):
#         read=readings_dict[str(sayi)]
#     elif sayi>=20 and sayi<100:
#         read+=readings_dict2[str(onlarBasamak(sayi))]+" "+readings_dict2[str(birlerbasamak(sayi))]
#
#     elif sayi>=100:
#         read+=readings_dict[str(yuzlerBasamak(sayi))]+" hundred"+readings_dict2[str(onlarBasamak(sayi))]+readings_dict[str(birlerbasamak(sayi))]
#
#     print(read)
#
#


# # basamakBelirle(482)
# print(yuzlerBasamak(100))
# print(onlarBasamak(100))
# print(birlerbasamak(100))