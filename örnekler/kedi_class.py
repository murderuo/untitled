class kedi():

    def __init__(self):
        pass
    def kunye(self,adi,yasi):
        self.ad=adi
        self.yas=yasi
        return self.ad,self.yas

    @staticmethod
    def kunye_goster(nesne):
        return nesne[0],nesne[1]



kedi1=kedi()

duman=kedi1.kunye("duman",2)



print( )
