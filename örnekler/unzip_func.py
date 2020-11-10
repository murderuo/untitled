'''verilen iki listedeki elemanları ikili tuple olarak tutar'''

'''zipleme kısmı'''

liste1=[1,2,3,4]
liste2=[5,6,7,8]

z =zip(liste1,liste2)

z_list=list(z) # listeye çeviriyoruz

print(z)  #ziplenmiş nesne

print(z_list)


'''
itere edildiğinde;
(1, 5)
(2, 6)
(3, 7)
(4, 8)
edilmeden kullanılırsa liste içinde ikili tuple ;
[(1, 5), (2, 6), (3, 7), (4, 8)]
'''


'''unzip etme kısmı DİKKAT!   UNZİP EDİLEN LSİTELER TUPLE OLARAK DÖNER '''

un_zip=zip(*z_list) #tuple nesnesi yaratıyoruz

un_list1,un_list2=list(un_zip) #unzip edilen tuple 'ı listeye çeviriyoruz

print(un_zip) ## nesne

print(un_list1)

print(un_list2)

print(type(un_list2))  #tipine bakıyoruz