


'''bir satırda liste elemanları ile iterasyon yapmamızı sağlar'''

liste1=[1,2,3,4]

square_list=[i**2 for i in liste1]

print(square_list)


'''örnek iki'''

liste2=[1,3,5,7,9]

comp_list=[i+4 if i<3 else i+3 if i<5 else i+9  for i in liste2]

print(comp_list) # [5, 6, 14, 16, 18]

'''örnek üç'''

liste2=[2,4,6,8]

print(liste2)

comp_list2=[i**2 if i==2 else i-6 if i==6 else i+8 if i==8 else i-4 for i in liste2]

'''örnek 4'''

liste3=[1,2,3,4,5,6,20,21]
print(liste3)

comp_list3=[i+1 if i<=3 else i+2 if i>3 and i<=6 else print("işlem yapılamadı") for i in liste3]

print(comp_list3)

