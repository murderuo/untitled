import time
start = time.time()
def asalCarpan(sayi):
    asalcarps=[]
    for s in range(2,sayi):
        while 1:
            if sayi%s == 0:
                k=sayi/s
                if k != 0:
                    sayi=k
                    asalcarps.append(s)
            elif sayi%s!=0:  break
    if asalcarps==[]: return [sayi]
    else: return asalcarps
print(asalCarpan(37289))
end = time.time()
print(end - start)