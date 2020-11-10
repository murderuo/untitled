import re
#
# NumRegex = re.compile(r'\d\d\d')
# dat=NumRegex.search(10)
# print(dat)

#
# print(phoneNumRegex)
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo)
# print('Phone number found: ' + mo.group())

readings=["one","two","three","four","five","six","seven","eight","nine","ten","ty",
          "eleven","twelve","thir","teen","fif","twenty","for","hundered"]

readings_dict={"1":["one","ten"],"2":["two","twen"],"3":["three","thir"],"4":["four","for"],"5":["five","fif"],
               "6":"six","7":"seven","8":"eight","9":"nine","0":"ty","11":"eleven","12":"twelve","t":"teen","100":"hundered"}

def ucbasamakKontrol(list):
    v=""
    if len(list)==3:
        if len(readings_dict[list[0]])==2:
            v=readings_dict[list[0]][0]
            v+=" "+readings_dict["100"]
        else:
            v=readings_dict[list[0]]
            v+=" "+readings_dict["100"]

    print(v)

def ikibasamakKontrol(lis):
    v=""
    if dat[0]=="1":
        if dat[1]=="0":
            v=readings_dict[dat[0]][1]
            print(v)
        if dat[1]=="1":
            v=readings_dict["11"]
            print(v)
        if dat[1]=="2":
            v=readings_dict["12"]
            print(v)



dat=re.findall("[0-9]","900")
print(dat)

ucbasamakKontrol(dat)
















# # print(len(readings_dict[dat]))
# if len(dat)==1:
#     if len(readings_dict[dat[0]])==2:
#         v=readings_dict[dat[0]][0]
#         print(v)
#     else:
#         v=readings_dict[dat[0]]
#         print(v)
# elif len(dat)==2:
#     if dat[0]=="1":
#         if dat[1]=="0":
#             v=readings_dict[dat[0]][1]
#             print(v)
#         if dat[1]=="1":
#             v=readings_dict["11"]
#             print(v)
#         if dat[1]=="2":
#             v=readings_dict["12"]
#             print(v)
#
#
#
#
#
#
#
#
#         # tmp=readings_dict[dat[0]][1]
#         # tmp+="ty"
#         # print(tmp)
