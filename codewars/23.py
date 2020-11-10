"""Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings.

-- We shall assign the following values: a = 1, b = 2 ... z = 26.

For example, for the word "zodiacs", solve("zodiacs") = 26
-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
Vowels are are a,e,i,o,u.

For C: do not mutate input."""

def solve(s):
    vvls="a,e,i,o,u"
    letters=" abcdefghijklmnopqrstuvwxyz"
    temp=value=0
    for l in s:
        if l in vvls:
            temp=0
            continue
        else:temp+=letters.index(l)
        if temp>value:value=temp
        else: continue
    return value







#a1 b2 c3 d4 e5 f6 g7 h8 i9 j10 k11 l12 m13 n14 o15 p16 q17 r18 s19 t20 u21 v22 w23 x24 y25 z26
print(solve("zodiac"))                            #,26)
print(solve("chruschtschov"))                     #,80)
print(solve("khrushchev"))                         #,38)
print(solve("strength"))                           #,57)
print(solve("catchphrase"))                        #,73)
print(solve("twelfthstreet"),)                     #103)
print(solve("mischtschenkoana"))                   #,80)