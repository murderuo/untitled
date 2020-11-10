class Test:
    def __init__(self):
        self._yeni_isim="ugur"
        self._nveri=0

    @property
    def isim(self):
        return self._yeni_isim

    @property
    def veri(self):
        return self._nveri

    @veri.setter
    def veri(self,yeni_deger):
        self._nveri=yeni_deger
        return self._nveri
    @veri.deleter
    def veri(self):
        del self._nveri


t=Test()
t.veri=5

print(t.isim,t.veri)

print(t._nveri)