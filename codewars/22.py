"""A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more capitals letters. The 1st letter of a code is the capital letter of the book category. In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

For example an extract of one of the stocklists could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or

L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

  M = {"A", "B", "C", "W"}
or

  M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket a list of pairs):

  (A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

If L or M are empty return string is "" (Clojure and Racket should return an empty array/list instead).

Note:
In the result codes and their values are in the same order as in M."""


def stock_list(listOfArt, listOfCat):
    vdict={}
    pdict={}
    prnt_value=""
    for c in listOfCat:
        v = 0
        for s in listOfArt:
            if s[0]==c:
                v+=int(s[s.index(" "):])
            else: vdict[c]=0
        vdict[c]=v
    # return vdict
    for c in listOfCat:
        pdict[c]=vdict.get(c)
    for k,val in pdict.items():
        prnt_value+="".join("({} : {}) - ".format(k,val))
    return prnt_value[:-3]
    # return pdict

b=['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
c=['A', 'B', 'C', 'D']
print(stock_list(b, c),"#####(A : 0) - (B : 1290) - (C : 515) - (D : 600)")#


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c),"####(A : 200) - (B : 1140)")#,

b=['CBART 20', 'CDXEF 50', 'BKWRK 25', 'BTSQZ 89', 'DRTYM 60']
c=['A', 'B', 'C', 'W']
print(stock_list(b, c),'######(A : 0) - (B : 114) - (C : 70) - (W : 0)')

b=['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
c=['B', 'R', 'D', 'X']
print(stock_list(b, c),'###(B : 364) - (R : 225) - (D : 60) - (X : 0)')

b=[]
c=['B', 'R', 'D', 'X']
print(stock_list(b, c)," " )

b=['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
c=[]
print(stock_list(b, c),"## ")

b=['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
c=['U', 'V', 'R']
print(stock_list(b, c),'####(U : 0) - (V : 0) - (R : 225)')