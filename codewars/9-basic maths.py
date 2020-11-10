def basic_op(operator, value1, value2):
    ops={"+":value1+value2,"-":value1-value2,"*":value1*value2,"/":value1/value2}
    return ops[operator]
    # ops={"operator":(lambda x,y:x+y),operator:(lambda value1,value2:value1-value2),
    #      operator:(lambda value1,value2:value1*value2),operator:(lambda value1,value2:value1/value2)}
    # return ops[operator](value1,value2)

print(basic_op('-', 15, 18))
# print(basic_op('*', 5, 5))

#
# def basic_op(op, v1, v2):
#     return v1+v2 if op == "+" else v1-v2 if op == "-" else  v1*v2 if op == "*" else  v1/v2