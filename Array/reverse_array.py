arr = [4,3,2,1]
rev_arr=[]

def reverse_array(arr):
    rev_arr=[]
    for i in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[i])
    return rev_arr

rev_arr=reverse_array(arr)
print(rev_arr)


"""
To reverse an array:
arr[::-1]
"""