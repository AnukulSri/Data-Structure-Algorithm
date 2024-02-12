## Bubble Sort Algorithm.
## Big O complexity of this algorithm is O(n^2)


def bubble_sort(arr,l):
    for i in range(l):
        for j in range(l-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr
arr = [4,5,2,6,1,7,8,0]
l = len(arr)
res = bubble_sort(arr,l)
print(res)