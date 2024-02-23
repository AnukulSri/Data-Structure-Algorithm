# Delete element from array..

arr = [1,2,3,4,5]
n = int(input("Enter a number to be removed "))


def delete_element(arr,n):

    
    if n not in arr:
        return "no such element present in array"
    new_arr=[]
    

    for i in range(len(arr)):
            if arr[i] != n:
                new_arr.append(arr[i])
    return new_arr

new_arr = delete_element(arr,n)
print(new_arr)
        
