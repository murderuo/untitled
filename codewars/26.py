"""There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings."""


def find_uniq(arr):
    temp=[]
    for i in arr:
        temp.append(list(sorted(set(i.lower()))))
    # # print(set(temp))
    # print(temp)
    # print(temp[0],temp[1],temp[2],sep="\n")
    # # temp2=list(sorted(set(temp)))
    for k in temp:
        if temp.count(k)==1:
            # print(temp)
            return arr[temp.index(k)]

print(find_uniq(['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']) )#           , 'BbBb')
# print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])     )#           , 'foo')
# print(find_uniq([ '    ', 'a', '  ' ])                                   )#              , 'a')