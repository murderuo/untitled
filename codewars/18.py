"""Complete the method which accepts an array of integers, and returns one of the following:

"yes, ascending" - if the numbers in the array are sorted in an ascending order
"yes, descending" - if the numbers in the array are sorted in a descending order
"no" - otherwise
You can assume the array will always be valid, and there will always be one correct answer."""

def is_sorted_and_how(arr):
    v=""
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            v='yes, descending'
        if arr[i] >= arr[i+1]:
            v='yes, asc'
        else:
            v="no"
    return v


















    value=""
    # for i,v in enumerate(arr):
    #     # print(i,v)
    #     if i+1 == len(arr):
    #         return a
    #     elif arr[i] >= arr[i+1] :
    #         a='yes, descending'
    #     elif arr[i] <= arr[i+1]:
    #         a='yes, ascending'
    #     else:
    #         a="no"

print(is_sorted_and_how([15, 7, 3, -8]))
print(is_sorted_and_how([1,2]))
print(is_sorted_and_how([4, 2, 30]))
