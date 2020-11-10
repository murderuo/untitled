def topla():
    '''iç içe fonksiyonlara verilen ada nested fonksiyon deniyor'''
    ''' iki sayıyı toplayacağız'''
    x=6
    y=5
    def cikar ():

        fark=x-y
        return fark
    return cikar() +5

print(topla())






