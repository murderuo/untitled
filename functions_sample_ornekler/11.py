kitaplar=[[10,'python'],[20,'test kitabı'],[30,'deneme']]

while 1:
    kitapNo=input('kitap no giriniz : ')
    if kitapNo not in ['ç','Ç']:
        for k in kitaplar:
          #  print (k)
            if int(kitapNo)==k[0]:
                print (k[0], 'nolu kitap', k[1])
                break
        else:
            print ('kitap bulunamadı')
    else:
        break
