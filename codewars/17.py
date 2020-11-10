"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in
Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.



"""
asd=95862

l=[]
def convert(num):
    print(l)
    if num<10:
        l.append(num)
        return l

    b1=num%10**(len(str(num))-1)
    num=num-b1
    l.append(num)
    convert(b1)


print(convert(asd))
# print(l)

# print(b1)
# num=num-b1
# print(num)

