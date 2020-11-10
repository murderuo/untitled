'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

numbers=[10, 15, 3, 7]
given_number=int(input("give me a number"))
summ=[]
for number in numbers:
    for n in numbers:
        check_sum=0
        if numbers==n:continue
        else:
            check_sum=number+n
            if not check_sum in summ:
                summ.append(check_sum)
if given_number in summ: print("your number is in the list")

