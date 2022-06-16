"""
Capture Regions on Board


Problem Description

Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Problem Constraints

1 <= N, M <= 1000



Input Format

First and only argument is a N x M character matrix A.



Output Format

Make changes to the the input only as matrix is passed by reference.



Example Input

Input 1:

 A = [ 
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X] 
     ]

Input 2:

 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]



Example Output

Output 1:

 After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]

Output 2:

 After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]



Example Explanation

Explanation 1:

 O in (4,2) is not surrounded by X from below.

Explanation 2:

 No O's are surrounded."""

"""
Hint 1

Note that all the chunks of O which remain as O are the ones which have at least one O connected to them which is on the boundary. Otherwise they will turn into X.

Think of graph traversal.

"""
"""
Solution Approach

We already know chunks of O which remain as O are the ones which have at least one O connected to them which is on the boundary.

Use BFS starting from ‘O’s on the boundary and mark them as ‘B’, then iterate over the whole board and mark ‘O’ as ‘X’ and ‘B’ as ‘O’.

Note: Don’t return any matrix. Do the changes in the given matrix.

"""

class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        from collections import deque
        def util(x , y):
            de = deque()
            de.append([x ,y])
            
            while de:
                tempx ,tempy = de.popleft()
                A[tempx][tempy] = '*'
                
                if  x < len(A)-1 and A[x+1 ][y] == 'O':
                    de.append([x+1, y])

                if x > 0 and A[x -1][y] == 'O':
                    de.append([x-1, y])

                if y < len(A[0])-1 and A[x ][y+1] == 'O':
                    de.append([x, y+1])

                if y > 0 and A[x ][y-1] == 'O':
                    de.append([x, y-1])
        r= len(A)
        c= len(A[0])
        
        for i in range(0, c):
            if A[0][i] == 'O':
                util(0, i)
                
        for i in range(1, r):
            if A[i][c-1] == 'O':
                util(i, c-1)
                
        for i in range(c-2, -1, -1):
            if A[r-1][i] == 'O':
                util(r-1, i)
                
        for i in range(r-1, -1,-1):
            if A[i][0] == 'O':
                util(i, 0)
        
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == '*':
                    A[i][j] = 'O'
                else:
                    A[i][j] = 'X'
                    
        # print("tes")
        # print(A)
        
        return A
                    