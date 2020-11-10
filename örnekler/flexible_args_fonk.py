def topla(*args):

    #fonksiyona bazen 1 bazen de 1 den fazla değer göndermek istediğimizde kullanılır
    #verilen değerler fonksiyona tuple olarak girer



    t=0
    for i in args:

        t=t+i

    return t

print(topla(6,7,9,0,-25))



def f(**kwargs):
    '''bir veya birden fazla değer gönderildiğinde kullanılır
    gönderilen değerler bir dictionary dir (sözlüktür), key ve value olarak gönderilmesi
    gereklmektedir.'''

    for item,deger in kwargs.items():
        print(item,deger)

f(istanbul="test", ankara=10,izmir=0.87)



