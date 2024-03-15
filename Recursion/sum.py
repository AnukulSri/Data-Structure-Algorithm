# doing sum of n numbers using recursion:

def sum(n):
    if n==1:
        return 1
    else:
        return n+ sum(n-1)
    
if __name__ == '__main__':
    n = int(input("Enter a number"))
    print(sum(n))

# the big O complexity of the code is linear, O(n).