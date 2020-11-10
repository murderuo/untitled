ogrenciler=[]
i=1
while 1:
    isim=input('öğrenci adını giriniz: ')
    soyisim=input('öğrencinin soyadını giriniz: ')
            
    if isim not in ['ç','Ç'] or isim not in ['ç','Ç'] :
        numara=int(input('numarasını giriniz.'))
        ogrenciler.append([isim,soyisim,numara,i])
        
    else:
        print ('çıkış yapıldı')
        break
    i=i+1
            
