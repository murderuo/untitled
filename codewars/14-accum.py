def accum(s):
    ns=s.lower()
    for l in ns:
        for i in range(-1,int(ns.index(l))+1):
            # print(int(ns.index(l)))
            if i==-1:
                print(l.upper(),end="")
                continue
            print(l,end="")
        print(end=" ")

accum("Nyff")



