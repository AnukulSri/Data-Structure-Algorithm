## linear search algorithm
## time complexity is O(n)

def linear_search(arr,n):
    l= len(arr)
    c=0
    for i in range(l):
        if arr[i] == n:
            print("Number is present in a list at index ",i)
            c+=1
            break
    if c == 0:
        print("Number is not in a list")
if __name__ == '__main__' :
    arr = [1,21,3,4,22,5,24]
    n = int(input("Enter a number to be searched"))
    linear_search(arr,n)