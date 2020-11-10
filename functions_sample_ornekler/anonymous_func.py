

'''bir listedeki elemanları lambda functionunda tek tek uygular'''
'''bir veya birden fazla değer alabilir (liste içinde)'''


sayilar=[1,3,5,7,9]

y =map(lambda x:x**2,sayilar)

print(list(y))