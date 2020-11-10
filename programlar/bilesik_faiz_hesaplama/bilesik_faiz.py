anapara=int(input("Hesaplanacak tutarı giriniz: "))
gunSayisi=int(input("Hesaplanacak gün sayısını giriniz: "))
faizOrani=float(input("Hesaplanacak oranı giriniz: "))
kacAy=int(input("Ne kadar süre ile uygulanacak: "))


for i in range(kacAy):
    faizTutari=(anapara*faizOrani*gunSayisi)/36500

    kesinti=faizTutari*(15/100)
    k=kesinti
    kalan=faizTutari-k
    print ('%d.ayda anapara %.2f TL, faiz miktari %.2f TL\'tir. Vade sonu toplam:%.2f TL' %(i+1,anapara,kalan,anapara+kalan))
    anapara=anapara+kalan
    
  
    

