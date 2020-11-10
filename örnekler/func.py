def kenar(a,b):
        if a >b:
            if a ==b: print("karedir")
            elif a < 0 and b<0: print("pozitif bir değer giriniz.")
            else:
                mod=a%b
                while mod!=0:
                    a=b
                    b=mod
                    mod=a%b
                print(b)
        else:
            print("Kısa uzun kenar değişimi yapılarak hesaplandı")
            c=0
            c=a
            a=b
            b=c
            kenar(a,b)

b=int(input("kısa kenarı giriniz:"))
a=int(input("uzun kenarı giriniz"))


kenar(a,b)