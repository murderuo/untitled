import time
start = time.time()
def asalCarpan(sayi):
    asalcarps=[]
    asalBolenler=[]
    if sayi==1 or sayi<=0: return [1]
    else:
        aralarindaki_asallar=[2]
        for i in range(1,sayi):
            if (2**i)%i==2:
                aralarindaki_asallar.append(i)
            else:continue
        # return aralarindaki_asallar
        for i in aralarindaki_asallar:
            if sayi%i==0:
                asalBolenler.append(i)
            else: continue
        # return asalBolenler
        if asalBolenler==[]:return [sayi]
        else:
            for i in asalBolenler:  #sayi=26  #asallari= 2,13
                while 1:
                    if sayi%i==0:
                        k=sayi/i
                        if k != 0:
                            sayi=k
                            asalcarps.append(i)
                    else: break
    return asalcarps
# print(asalCarpan(43))
print(asalCarpan(37289))
end = time.time()
print(end - start)