print ("bir sayı seç")
print ("iki şansınız var")

durum=True
i=1
while i<=2:
    print (i,' .şans')
    girilen=input('bir sayı giriniz: ')
    #sayi=int(girilen)
    if girilen == '4':
        print ("tbr kanks :)) ")
        durum=False
        #break
    i=i+1
#else:

if durum==True:
    print ("2 şansını da denedin...")
else:
    print("iyisin hacı")
