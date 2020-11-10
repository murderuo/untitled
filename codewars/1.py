
def createDict():
    dict={}
    letters='abcdefghijklmnopqrstuvwxyz'
    for i,l in enumerate(letters):
        dict[l]=i+1
    return dict

createDict()
#
# def alphabet_position(text):
#     dict=createDict()
#     check=[" ","\'","\"","!",".","?"]
#     strng=""
#     for l in text:
#         print(l,end=" ")
#         if l.lower() in check: continue
#         strng+=str(dict[l.lower()])
#         print(strng)
#
#     return strng

# alphabet_position("The sunset sets at twelve o' clock.")
# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def alphabet_position(text):
    dict=createDict()
    check=[" ","\'","\"","!",".","?"]
    text_list=list(text.lower())
    # print(text_list)
    strn=""
    # print(text_list)
    for i in text_list:
        if i in check: continue
        # print(i,end=" ")
        strn+=str(dict[i])

    return strn

alphabet_position("The sunset sets at twelve o' clock.")


