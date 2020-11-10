def sum_array(arr):
    return sum(arr)-(min(arr)+max(arr)) if arr!=None and len(arr)!=1 and len(arr)!=0  else 0