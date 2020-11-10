def array_diff(a, b):
    if len(a)!=0:
        tmp=a.copy()
        for i in a:
            if i==b[0]:
                tmp.remove(i)
        return tmp
    else: return a