'''iterable nesnelerde iterate yapmaya yarar'''

nesne="bu_bir_iterable_nesnedir"

it=iter(nesne)

# for i in it:    for i in nesne:               ikisi de aynı işlevi görüyor
#     print(i)      #     print(i)


print("iterate yapılabilecek ilk nesne",next(it))

print("ardı ardına itere edilmiş hali:",next(it))

print("ardı ardına itere edilmiş hali:",next(it))

print("ardı ardına itere edilmiş hali:", *it)
