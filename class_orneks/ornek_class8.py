class Sorgu():
    def __init__(self, değer=None, sıra=None):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim','Metis'),
        ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim','İthaki'),
        ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt','Cem')]
        if not değer and not sıra:
            l = self.liste
        else:
            l = [li for li in self.liste if değer == li[sıra].lower()]
        for i in l:
            print(*i, sep=', ')
    @classmethod
    def isbnden(cls, isbn):
        cls(isbn, 0)
    @classmethod
    def yazardan(cls, yazar):
        cls(yazar.lower(), 1)
    @classmethod
    def eserden(cls, eser):
        cls(eser.lower(), 2)
    @classmethod
    def yayınevinden(cls, yayınevi):
        cls(yayınevi.lower(), 3)

ara=Sorgu()

ara.yayınevinden("Metis")
