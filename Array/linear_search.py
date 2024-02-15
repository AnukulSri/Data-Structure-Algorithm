# Linear search is a simplest approach employed to search element in a dataset.
# Time complexity of linear search algorithm is O(n).

def linear_search(arr,n):
    c = 0
    for i in range(len(arr)):
        if arr[i] == n:
            c = i
            break
    if c !=0 :
        print("number is found at index ",c)
    else:
        print("Number not found")



arr = [22,23,21,76,98,65]
n = int(input("Enter a number to be searched"))
linear_search(arr,n)


# The space complexity of the provided linear search code is constant, denoted as O(1).
# This is because the amount of additional memory used by the algorithm remains constant, regardless of the size of the input array.
