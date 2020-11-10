canta =['kalem','silgi','defter','kitap']

s=0
while True:
    x=input('çantada ne var ?')
    if x in canta:
        print ('brvo bildiniz.')
    else:
        canta.append(x)
        break
print (canta)
