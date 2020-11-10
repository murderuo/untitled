


'''verilen iki listedeki elemanları ikili tuple olarak tutar'''

liste1=[1,2,3,4]
liste2=[5,6,7,8]

z =zip(liste1,liste2)

z_list=list(z)

print(z)

print(z_list)
print(z_list[1][1])


'''
itere edildiğinde;
(1, 5)
(2, 6)
(3, 7)
(4, 8)
edilmeden kullanılırsa liste içinde ikili tuple ;
[(1, 5), (2, 6), (3, 7), (4, 8)]

'''