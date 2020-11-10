import dbm

db=dbm.open("moviedb","c")
# db["Ragtime"]=[]
db["Ragtime"]='Stretton, Ellen' #,'Rapp, Ilana']
db["key1"]="value1"
db["key2"]="value2"
db["key3"]="value3"
print(db.items())
# print(db.get("key3"))

# for i in db.values():
#     print(i)




# print(db["Ragtime"])
# print(db)
# db["Ragtime"]+=

# for i in db["Ragtime"]:
#     print(i)

# for key in db.values():
#     print(key)

# print(db["Ragtime"])
# k = db.firstkey()
# while k != None:
#     print(k)
#     k = db.nextkey(k)


db.close()