def returntest():

    ad="ugur"
    soyad="okur"
    gorev="programcı"
    return ad,soyad,gorev

def getReturn(*args):
    ad,soyad,gorev=args
    print(ad,soyad,gorev)



returnTest=returntest()

getReturn(*returntest())
# print(returnTest)
