class Giris():
    def __init__(self,mesaj="Müşteri numaranızı giriniz :"):
        mNo=input(mesaj)
        print("hoş geldiniz")

    @classmethod
    def parolaileGir(cls):
        mesaj="lütfen parolanızı giriniz"
        cls(mesaj)
    @classmethod
    def TcnoileGir(cls):
        mesaj="lütfen tc numaranızı giriniz"
        cls(mesaj)


Giris.parolaileGir()




# login=Giris()