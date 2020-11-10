def fn1():
    print ("One")

def fn2():
    print ("Two")

def fn3():
    print ("Three")

fndict = {"A": fn1, "B": fn2, "C": fn3}

keynames = ["A", "B", "C"]

fndict[keynames[1]]()