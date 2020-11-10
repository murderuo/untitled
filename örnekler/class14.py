class Sinif:
    nitelik="sınıf niteliği"
    def __init__(self):
        self.nitelik="örnek niteliği"


Sinif.nitelik="sınıf değeri değişti"


print(Sinif.nitelik)

ornek=Sinif()

print(ornek.nitelik)

ornek.nitelik="örneğin 1 içindeki nitelik değişti"

print(ornek.nitelik)

ornek2=Sinif()

ornek2.nitelik="örnek 2 niteliği"

print(ornek2.nitelik)