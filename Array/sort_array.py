# Sort an array

"""
Input: l = [3,21,1,30,45,0]
Output: [0,1,3,21,30,45]
"""

arr = list(map(int,input().split()))
l = len(arr)
temp=0
for i in range(l):
    for j in range(i+1,l):
        if arr[j] < arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)

# time complexity will be O(n^2)