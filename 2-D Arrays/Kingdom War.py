"""Kingdom War

Two kingdoms are on a war right now, kingdom X and kingdom Y. As a war specialist of kingdom X, you scouted kingdom Y area.

A kingdom area is defined as a N x M grid with each cell denoting a village. Each cell has a value which denotes the strength of each corresponding village. The strength can also be negative, representing those warriors of your kingdom who were held hostages.

There's also another thing to be noticed.

    The strength of any village on row larger than one (2<=r<=N) is stronger or equal to the strength of village which is exactly above it.
    The strength of any village on column larger than one (2<=c<=M) is stronger or equal to the strength of vilage which is exactly to its left. (stronger means having higher value as defined above).

So your task is, find the largest sum of strength that you can erase by bombing one sub-matrix in the grid.

Input format:

First line consists of 2 integers N and M denoting the number of rows and columns in the grid respectively.
The next N lines, consists of M integers each denoting the strength of each cell.

1 <= N <= 1500
1 <= M <= 1500
-200 <= Cell Strength <= 200

Output:

The largest sum of strength that you can get by choosing one sub-matrix.

Example:

Input:
3 3
-5 -4 -1
-3 2 4
2 5 8

Output:
19

Explanation:
Bomb the sub-matrix from (2,2) to (3,3): 2 + 4 + 5 + 8 = 19
"""
"""
Hint 1
A simple observation is to notice that the strength on each row is larger or equal to the row above and the strength on each column is also larger or equal to the column on its left.

This means, we don’t really need to check every single sub-array.

    Note: Using Kadane’s 2D Max Sub-Matrix Sum O(N^3) will lead to TLE

    Note 2: Maximum answer might be negative.

"""
"""
Solution Approach
Based on the observation in Hint 1, we can assume that the largest sub-array strength may start from any point, but will definitely end on bottom-right cell (N,M).

Therefore, we can use dynamic programming to find the sum of sub-matrix starting from the bottom-right cell (N,M) going up and left.

DP[i][j] = DP[i+1][j] + DP[i][j+1] - DP[i+1][j+1]
Find the maximum answer from DP[i][j] for each (i,j)

"""
""" accepted solution """
# @param A : list of list of integers
# @return an integer
def solve(self, A):
    for i in range(len(A)):  # suffix row sum
        for j in range(len(A[0])-1,0,-1 ):
            A[i][j-1] += A[i][j]
                
    for i in range(len(A)-1,0,-1):  # suffix col sum
        for j in range(len(A[0])):
            A[i-1][j] += A[i][j]

    max_ = A[0][0]
    for i in range(len(A) ):
        for j in range( len(A[0]) ):
            if A[i][j] > max_:
                max_= A[i][j]
    
    return max_
