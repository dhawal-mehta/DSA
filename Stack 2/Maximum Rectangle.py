"""
Maximum Rectangle

Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.

Find the largest rectangle containing only 1's and return its area.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.


Input Format

The only argument given is the integer matrix A.

Output Format

Return the area of the largest rectangle containing only 1's.

Constraints

1 <= N, M <= 1000
0 <= A[i] <= 1

For Example

Input 1:
    A = [   [0, 0, 1]
            [0, 1, 1]
            [1, 1, 1]   ]
Output 1:
    4

Input 2:
    A = [   [0, 1, 0, 1]
            [1, 0, 1, 0]    ]
Output 2:
    1
"""
# @param A : list of list of integers
# @return an integer

    
def solve(self, A):

    def getMaxArea( A):
        stk = []
        index = 0
        max_area = 0
        while index < len(A):
            if not stk or A[stk[-1]] <= A[index]:
                stk.append(index)
                index+=1
            else:
                temp = stk.pop()
                area = A[temp]*((index - stk[-1] -1 ) if stk else index)
                max_area = max(area, max_area)

        while stk:
            temp = stk.pop()
            area = A[temp]*((index - stk[-1] -1 ) if stk else index)
            max_area = max(area, max_area)
        
        return max_area


    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != 0:
                A[i][j] = (A[i][j] + A[i-1][j] if i != 0 else A[i][j] )
    

    max_area = 0
    
    for i in A:
        area = getMaxArea(i)
        max_area = max(area, max_area)

    return max_area
                