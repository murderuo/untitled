def asal_sayi(sayi):
    for i in range(2,sayi):
        for j in range(2,i):
            if i % j ==0:
                break
            elif(i % j!=0) and (j ==i -1):
                print(i)
            
            
            
asal_sayi(100)
