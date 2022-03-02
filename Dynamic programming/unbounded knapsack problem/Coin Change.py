"""
Coin Change

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, 
for N = 4 and S = {1,2,3}, 
there are four solutions: {1,1,1,1}, {1,1,2}, {2,2} and {1,3}. 
So output should be 4. 

For N = 10 and S = {2, 5, 3, 6}, 
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
So the output should be 5.

"""

# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):

#----------------using 2d dp --------------------------
    # table = [[0 for y in range(n+1)] for x in range(m+1)]
 
    # for i in range(m):
    #     table[i][0] = 1
 
    # for i in range(1,m):
    #     for j in range(1,n+1):

    #         x = table[i-S[j]][j] if i >= S[j] else 0

    #         y = table[i-1][j]

    #         table[i][j] = x + y
 
    # return table[-1][-1]

    t = [0 for i in range(n+1)]
 
    t[0] = 1
 
    for i in range(1,n+1):
        for j in range(m):
            if S[j] >= i:
                t[i] += t[i-S[j]]
 
    return t[n]
 
# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))
