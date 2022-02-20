"""
Unique Paths III


Problem Description

Given a matrix of integers A of size N x M . There are 4 types of squares in it:

1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.

Find and return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

2 <= N * M <= 20
-1 <= A[i] <= 2


Input Format

The first argument given is the integer matrix A.


Output Format

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.


Example Input

Input 1:

A = [   [1, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 2, -1]   ]

Input 2:

A = [   [0, 1]
        [2, 0]    ]



Example Output

Output 1:

2

Output 2:

0



Example Explanation

Explanation 1:

We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Explanation 1:

Answer is evident here.
"""
"""
Hint 1

Think about the the brute force solution.

At every square we have atmost 4 directions to move So, the time complexity of the brute force solution is O(4 N*M).
"""
"""
Solution Approach

We can perform the dfs from the starting square and maintain a visited matrix to walk every non-empty square exactly once.

When we reach the ending square by visiting all the non-empty squares, increment the answer.

We can use backtracking technique to find all possible walks.

Time complexity of the solution: O(4 N*M) because at every possible square we can move in 4 directionns.

This time complexity will give TLE but bad walks (walks which will not contribute to the answer) tend to stuck quickly and run out of free squares which make this solution to pass in the given input limits.
"""
xx = [1, 0, 0, -1]
yy = [0, 1, -1, 0]
def isV(u, v, A):
    return 0 <= u and u < len(A) and 0 <= v and v < len(A[0]) and A[u][v] != -1

def recur(x, y, cnt, A):
    if  A[x][y] == 2: 
        if cnt == 0:
            return 1
        return 0
    A[x][y] = -1
    ans = 0
    for i in range(4): 
        u = x + xx[i]
        v = y + yy[i]
        if isV(u, v, A): 
           ans += recur(u, v, cnt - 1, A)
    A[x][y] = 0
    return ans
    
class Solution:
# @param A : list of list of integers
# @return an integer
    def solve(self, A):
        ans = 0
        u, v, cnt = -1, -1, 0
        for i in range(len(A)):
            for j in range(len(A[0])): 
                if  A[i][j] == 1: 
                    u = i    
                    v = j
                elif A[i][j] == 0:
                    cnt += 1
        assert(u != -1)
        return recur(u, v, cnt + 1, A)