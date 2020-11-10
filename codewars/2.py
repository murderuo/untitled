# def get_sum(a,b):
#     t=0
#     for i in range(a,b+1):
#         if a==b: return a
#         t+=i
#     return t
# get_sum(1,1)

def get_sum(a,b):
    return sum(range(min(a,b), max(a,b)+1))
print(get_sum(1,100))





#     # x=lambda a,b,t=0:a else t=t+i if a==b for i in range(a,b+1)
#     # return x(a,b)
#     # x=lambda a,b: (for i in range(a,b+1):print(i))
#     values=lambda a,b,t=0: [i for i in range(a,b+1) ]
#     print( x(2,9))


    # print([for i in range(a,b+1) t=t+i ])





#good luck!
# get_sum(1,0) == 1//1+0=1
# get_sum(1,2) == 3//1+2=3
# get_sum(0,1) == 1//0+1=1
# get_sum(1,1) == 1//1
# Since
# both
# are
# same
# get_sum(-1,0) == -1//-1+0=-1
# get_sum(-1,2) == 2//-1+0+1+2=2

# values=lambda a,b,t=0: [t+=i for i in range(a,b+1) ]
# print(values)