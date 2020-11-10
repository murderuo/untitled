def asalBul2(i,n):
    temp=[]

    for i in range(i,n):
        asal=True
        for j in range(1,i+1):
            if i%j==0:
                asal=False
        if asal==True:
            temp.append(i)
    return temp



def asalBul(i,n):
    temp=[]

    for i in range(i,n):
        if i==2:
            temp.append(i)
            continue
        elif i%2==1:
            for j in range(1,i) :
                # if j%2==0:
                if i%3==0 and i%5==0:  #[2, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
                            #[2, 5, 7, 11, 13, 17, 19, 23, 25, 25, 29, 31, 35, 35, 35, 37, 41, 43]
                    continue
                elif i%j==0:
                    temp.append(i)


    return temp
# setted=set(asalBul(1,13))
print(asalBul(1,14))
# print(asalBul2(1,14))