## Selection Sort Algorithm.
# Its Big O complexity is O(n^2)

def sorting(arr,l):
    temp =0
    for i in range(l):
        for j in range(i+1,l):
            if arr[j] < arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

arr = list(map(int,input().split()))
l = len(arr)
res = sorting(arr,l)
print(res)
