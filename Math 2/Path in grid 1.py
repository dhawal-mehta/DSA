"""
Path in grid 1

Count all possible paths from top left to bottom right of a mXn matrix

The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down
Examples : 
 

Input :  m = 2, n = 2;
Output : 2
There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)

Input :  m = 2, n = 3;
Output : 3
There are three paths
(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)
(0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
(0, 0) -> (1, 0) -> (1, 1) -> (1, 2)
"""


##------------------------------------------ Recursive Solution -------------------------------------------------
# function to return count of possible paths
# to reach cell at row number m and column
# number n from the topmost leftmost
# cell (cell at 1, 1)
def numberOfPaths(m, n):

    if(m == 1 or n == 1):
        return 1
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)


##------------------------------------------ DP Solution -------------------------------------------------
# Returns count of possible paths to reach cell
# at row number m and column number n from the
# topmost leftmost cell (cell at 1, 1)
def numberOfPaths(m, n):

     
    count = [[0 for x in range(n)] for y in range(m)]
   
    for i in range(m):
        count[i][0] = 1
   
    for j in range(n):
        count[0][j] = 1
   
    for i in range(1, m):
        for j in range(1, n):            
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[m-1][n-1]

##------------------------------------------ DP Solution with sapce optimization -------------------------------------------------
def numberOfPaths(p, q):
     
    # Create a 1D array to store
    # results of subproblems
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]

##------------------------------------------ Combinatorics solution  -------------------------------------------------
def numberOfPaths(m, n) :
 
    # We have to calculate m + n-2 C n-1 here
    # which will be (m + n-2)! / (n-1)! (m-1)! path = 1;
    for i in range(n, (m + n - 1)):
        path *= i
        path //= (i - n + 1)
     
    return path