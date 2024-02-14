# Insertion sort algorithm.
# TIme complexity is O(n^2)

def insertion(arr):
    for i in range(1,l):
        k = arr[i]
        j=i-1

        while j>=0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = k
         
arr = [64,25,12,22,11]
l = len(arr)
insertion(arr)
print(arr)