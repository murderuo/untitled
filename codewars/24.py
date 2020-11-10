"""len(a) will give you the number of top-level elements in the list/array named a.

Your task is to create a function deepCount that returns the number of ALL elements within an array, including any within inner-level arrays.

For example:

deepCount([1, 2, 3]);
//>>>>> 3
deepCount(["x", "y", ["z"]]);
//>>>>> 4
deepCount([1, 2, [3, 4, [5]]]);
//>>>>> 7
The input will always be an array."""

def deep_count(a):
    value=0
    for i in a:
        value+=1
        if type(i)==list:
            value+=deep_count(i)
    return value





# print(deep_count([]))                          #, 0, "Expected 0")
# print(deep_count([1, 2, 3]))                   #, 3, "Expected 3")
print(deep_count(["x", "y", ["z"]]))           #, 4, "Expected 4")
# print(deep_count([1, 2, [3, 4, [5]]]))         #, 7, "Expected 7")
# print(deep_count([[[[[[[[[]]]]]]]]]))          #, 8, "Expected 8")
