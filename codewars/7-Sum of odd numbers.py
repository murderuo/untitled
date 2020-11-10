# 1
# 3,5               2*1+1,  2*2+1                               =8
# 7,9,11            2*3+1,  2*4+1,  2*5+1                       =27
# 13,15,17,19       2*6+1,  2*7+1,  2*8+1,  2*9+1               =64
# 21,23,25,27,29    2*9+1,  2*10+1, 2*11+1, 2*12+1, 2*13+1      =115

#
def addRow(n):
    total=0
    for i in range(n):total+=i
    firsNum=2*total+1

    sum=0
    for j in range(n):
        sum+=firsNum
        firsNum+=2
        print(firsNum)

    # print(sum)

addRow(5)




















# for i in range(19):
#     # print(i)
#     for j in range(i):
#         if i%2==1:
#             print(i,end=" ")

