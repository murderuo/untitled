x=["Ryan", "Kieran", "Mark"]
# for i in x:
#     print(i)

def friend(l):
    print( [i for i in l if len(i)==4 ])
friend(x)
