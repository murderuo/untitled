"""There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance."""



def find_uniq(arr):
    setted_arr=list(set(arr))
    return [i for i in setted_arr if arr.count(i) == 1][0]