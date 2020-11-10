

while 1:

    try:

        anapara=float(input("Hesaplanacak tutarı giriniz: "))
        gunSayisi=int(input("Hesaplanacak gün sayısını giriniz: "))
        faizOrani=float(input("Hesaplanacak oranı giriniz: "))
        kacAy=int(input("Ne kadar süre ile uygulanacak: "))
    except:
        print("Geçerli bir değer girilmedi")

    else:


        for i in range(kacAy):

            faizTutari=(anapara*faizOrani*gunSayisi)/36500

            #kesinti=faizTutari*(5/100) #31/08/2018 den sonra %15 olan kesinti oranı %5 olarak değişmiştir.

            kalan=faizTutari#-kesinti
            print ('%d.ayda anapara %.2f TL, faiz miktari %.2f TL\'tir. Vade sonu toplam: %.2f TL' %(i+1,anapara,kalan,anapara+kalan))
            anapara=anapara+kalan+100




  
    



#print ('%d miktar paranın faizi %.2f dir.kesinti %.2f , kalan %.2f dir' % (anapara,faizTutari,kesinti,kalan))
