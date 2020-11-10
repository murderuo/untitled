liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def sorgula(olcut=None,deger=None):
    for li in liste:
        if not olcut and not deger:
            print(*li,sep=", ")
        elif olcut=="isbn" and deger==li[0].lower():
            print(*li,sep=", ")
        elif olcut=="yazar" and deger==li[1].lower():
            print(*li,sep=", ")
        elif olcut=="kitap" and deger==li[2].lower():
            print(*li,sep=", ")
        elif olcut=="yayinevi" and deger==li[3].lower():
            print(*li,sep=", ")


sorgula("kitap","böyle buyurdu zerdüşt")

# for li in liste:
#     print(*li,sep=", ")