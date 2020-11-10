def positive_sum(arr):
    if len(arr)!=0:  return (sum([i for i in arr if i>0]))
    return 0

positive_sum([])

positive_sum([-1,2,3,4,-5])