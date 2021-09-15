"""
Search in a row wise and column wise sorted matrix

Problem Description
Given a matrix of integers A of size N x M and an integer B.

In the given matrix every row and column is sorted in increasing order. Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.


Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
-100000 <= B <= 100000


Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.


Output Format
Return the position of B and if it is not present in A return -1 instead.


Example Input
A = [ [1, 2, 3]
          [4, 5, 6]
          [7, 8, 9] ]
B = 2


Example Output
1011


Example Explanation
A[1][2]= 2
1*1009 + 2 =1011 
"""
"""
Hint 1
you can use two loops in the array A and search if A[i][j] matches with B.
"""
"""
Solution Approach
You can use two loops in the array A outer loop i:1 to n and inner loop j:1 to n
and search if A[i][j] matches with B.
If there are multiple B return the smallest value i*1009 + j.
"""
"""accepted solution """
# @param A : list of list of integers
# @param B : integer
# @return an integer
def solve(self, A, B):
    
    i=0
    j=len(A[0])-1
    while(True):
        if(j < 0 or i >= len(A)):
            return -1
            
        else:
            if A[i][j] == B:
                while j>=0 and A[i][j]==B:
                    j-=1
                    
                return 1009*(i+1) + j+2
            if A[i][j] > B:
                j -= 1
            elif A[i][j] < B:
                i += 1