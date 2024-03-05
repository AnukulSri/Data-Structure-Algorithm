# Transpose matrix :
#l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# output :
"""
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16
"""

l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[j][i],end=' ')
    print()