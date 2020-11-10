'''
The input is a string str of digits.
Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk
if its size is less than sz).
If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
If sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible
to take a chunk of size sz hence return "".
Examples:
revrot("123456 9 87654", 6) --> "23456 1 876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "4466 8753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> ""
revrot("563000655734469485", 4) --> "0365065073456944"'''


def revrot(strng, sz):
    def check_chunk(val,sz):
        t=0
        for i in val: t=t+int(i) ** 2
        if t%2 == 1: return val[1:sz]+val[:1]
        else: return val[::-1]
    # your code
    if strng=="" or sz<=0: return ""
    pcs=len(strng)//sz
    if pcs*sz>len(strng): return ""
    else:
        s=""
        for p in range(pcs): s=s+check_chunk(strng[sz*p:sz*(p+1)],sz)
        return s

# print(revrot("1234", 0))
# print(revrot("1234", 5))
print(revrot("733049910872815764", 5))
"""revrot("5630=70// 0065=61 // 5734=99 // 4694=149// 85", 4) 
           0365      0650       7345       6944
0365 0650 7345 6944"""


"""73304=83//99108=227 // 72815=143   764"""
"""33047     91089        28157   """