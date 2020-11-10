import re
l="Sutherland, Donald (I) (1978) JFK [Prof. Dave Jennings]"
# tmp=[]
a_name=re.findall("^[A-Z].+\s+\(",l)
# a_name[0]=a_name[0].replace("(","").replace(")","").strip()

years=re.findall("\(\d.+\)",l)
# years[0]=years[0].replace("(","").replace(")","").strip()

movie_name=re.findall("\)\s[A-Za-z].*\[",l)
# movie_name[0]=movie_name[0].replace(")","").replace("[","").strip()

char_name=re.findall("\[.+\]",l) #character name
char_name[0]=char_name[0].replace("[","").replace("]","").strip()


character_name=re.findall("\[.*\]",l)

print(a_name,years,movie_name,char_name,sep="\n")
# tmp1=l.split()
#
# for i in tmp1:
#     k=re.findall("\)",i)
#     tmp.append(k)
# print(tmp)

# emptylist=[]
# print(len(emptylist))
























# import sqlite3
# import os
#
#
# while True:
#
#     giris=input("input bekleniyor:")
#     print("input alındı:",giris)
#
#     sql=f"CREATE TABLE personel (numara INTEGER PRIMARY KEY AUTOINCREMENT, ad VARCHAR, soyad VARCHAR, " \
#         f"tc INTEGER , oda INTEGER ,dah INTEGER ) "
#
#     file="sample.db"
#     # val=("ad","soyad","tc","odano","dah",)
#     if os.path.exists(file): continue
#     else:
#         con=sqlite3.connect(file)
#         cur=con.cursor()
#         cur.execute(sql)
#         con.commit()
#         con.close()



# Traceback (most recent call last):
#   File "/temp.py", line 12, in <module>
#     cur.execute(sqlite3,val)
# ValueError: operation parameter must be str




























# def is_isogram(string):
#     if "" in string or string.isalpha():
#         if len(list(string.lower()))==len(list(set(string.lower()))): return True
#         else: return False
#     else:return False
#
# print(is_isogram("Dermatoglyphics"),)
# print(is_isogram("isogram"))
# print(is_isogram("aba"))
# print(is_isogram("moOse"))
# print(is_isogram("isIsogram"))
# print(is_isogram(""))

# my_args=""
# my_args=('data', 'personel', 'ad', 'soyad', 'tc', 'oda', 'dah',)
#
# def arg_test(*args):
#     print(*args)
#
# arg_test(my_args)
# class deneme:
#     pass
#
#
#
# global test
#
# test = deneme()
# print(test)
#
#
# dict_vec = {'x': 1, 'y': 0, 'z': 1}
# v=(**dict_vec.values())
# print()








# def test(*args):
#     if str not in args:
#         print("str value does not exist")
#     else:
#         print("all args are str")
#
#
# test("burgaz","adam","smit")

# value="test"
# giris=input("pls input:")
# if giris=="":
#     giris=value
#
#
# print(giris)



