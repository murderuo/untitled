

while 1:

    try:

        anapara=float(input("Hesaplanacak tutarı giriniz: "))
        gunSayisi=int(input("Hesaplanacak gün sayısını giriniz: "))
        faizOrani=input("Hesaplanacak oranı giriniz: ")
        faizOrani=input("Hesaplanacak oranı giriniz: ")
        if "," in faizOrani:
            faizOrani.replace(",",".")
            faizOrani=float(faizOrani)
        else:
            faizOrani=float(faizOrani)
        kacAy=int(input("Ne kadar süre ile uygulanacak: "))
    except:
        print("Geçerli bir değer girilmedi")

    else:


        for i in range(kacAy):

            faizTutari=(anapara*faizOrani*gunSayisi)/36500

            kesinti=faizTutari*(20/100) #31/08/2018 den sonra %15 olan kesinti oranı %5 olarak değişmiştir.
			#döviz için %20 kesinti
			#tl için %15 kesinti

            kalan=faizTutari-kesinti
            print ('%d.ayda anapara %.2f TL, faiz miktari %.2f TL\'tir. Vade sonu toplam: %.2f TL' %(i+1,anapara,kalan,anapara+kalan))
            anapara=anapara+kalan#+100


    devam=input("Çıkmak için q ya bas:")
    if devam.lower()=="q":
        break
    else:continue




  
    



#print ('%d miktar paranın faizi %.2f dir.kesinti %.2f , kalan %.2f dir' % (anapara,faizTutari,kesinti,kalan))
