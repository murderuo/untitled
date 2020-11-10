anapara=float(input("Hesaplanacak tutarı giriniz: "))
##gunSayisi=180 #int(input("Hesaplanacak gün sayısını giriniz: "))
zamOrani=float(input("Hesaplanacak oranı giriniz: "))
kacAy=int(input("Ne kadar süre ile uygulanacak[yıl]: "))
zamDonemi=kacAy*2

for i in range(zamDonemi):
    zam=anapara*(zamOrani/100)
    zamliTutar=anapara+zam
    
    
##    k=kesinti
##    fark=faizliTurar-k
    print ('%d.donemde anapara %.2f TL, zam miktari %.2f TL\'tir. Vade sonu toplam: %.2f TL' %(i+1,anapara,zam,zamliTutar))
    anapara=zamliTutar

input()
  	
    



#print ('%d miktar paranın faizi %.2f dir.kesinti %.2f , kalan %.2f dir' % (anapara,faizTutari,kesinti,kalan))
