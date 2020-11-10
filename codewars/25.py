"""A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e")."""
"""Example
abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!" """

def my_abbreviate(s):
    temp=0
    if len(s)<=3: return s
    for i in range(1,len(s),1):
        if i==1:continue
        else:
            temp+=1
            if i ==len(s):break
    value=s[0]+str(temp)+s[-1:]
    return value

def abbreviate(s):
    temp=""
    mystring=""
    if s.isalpha():
        return my_abbreviate(s)
    else:
        for i in s:
            if i.isalpha():
                temp+=i
            else:
                mystring+=my_abbreviate(temp)+i
                temp=""
        return mystring


print(abbreviate("elephant-ride"))

