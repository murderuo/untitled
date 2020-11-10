txt_file=("sample.txt")
with open(txt_file,"r",encoding="utf-8") as f:
    try:
        all_words=f.read() # dosyayı okuma modunda açıyoruz, eğer bir hata alırsak
    except:
        print("dosya okunamadı") #hata alırsak dosya okunamadı hatasını veriyoruz
    else:                       #hata almazsak kodumuza devam ediyoruz
        all_words_list=all_words.strip().split()
        cntr=0
        for w in all_words_list:
            print(w.upper(),end=" ")
            cntr+=1
            if cntr==20:
                print("")
                cntr=0
            # elif cntr==40: print()
            # elif cntr==60:print()
            # elif cntr==80



