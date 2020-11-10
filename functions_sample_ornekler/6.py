print ("programdan çıkmak  için ç harfine basınız.")
while True:
    i=input("karekökü alınacak sayıyı giriniz : ")
    if i=='ç':
        print ("ç harfine bastınız ve döngüden çıktınız.")
        #break
    if int (i)<0:
        print ("negatif bir sayı girdiniz. hesaplama yapılamadı")
        #continue
    k=int(i)**(1/2)
    print ("girilen sayının karekökü: ",k)
