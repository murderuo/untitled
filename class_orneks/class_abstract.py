from abc import ABC,abstractmethod
# 1-abstractmethod dosyasını import etmek gerekiyor
# 2-ardından parent class içinde @abstractmethod decoratorunu kullanmamız gerekiyor
# 3-abstract olan parent classtaki herhangi bir methodu child classta kullanmak gerekiyor

class Animal:
    @abstractmethod
    def run(self):pass

    def walk(self):
        print("bird is walking")


class Bird(Animal):

    def __init__(self):
        print("bird created")



    def run(self):
        print("will run")

b=Bird()
b.walk()


