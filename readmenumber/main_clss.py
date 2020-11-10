readings_dict={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight",
               "9":"nine","10":"ten","11":"eleven","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen",
               "16":"sixteen","17":"seventeen","18":"eighteen","19":"nineteeen"}
readings_dict2={"2":"twenty","3":"thirty","4":"forty","5":"fifty",
                "6":"sixty","7":"seventy","8":"eighty","9":"ninety"}

def writeMe(sayi,before=""):
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
        # print(ob)
        writeMe(ob,read)


if __name__ == '__main__':


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

        writeMe(sayi)