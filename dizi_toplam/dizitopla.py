


def faktoriyel(n):
    carpim=1
    for i in range(n,1,-1):
        carpim=carpim*i
    return carpim



toplam=0
n=int(input("Bir sayı giriniz: "))
for j in range(1,n+1):
    toplam+=1/faktoriyel(j)
#     print(toplam)
#
print(toplam)
#
# print(faktoriyel(1))





