"""
Distance of nearest cell


Problem Description

Given a matrix of integers A of size N x M consisting of 0 or 1.

For each cell of the matrix find the distance of nearest 1 in the matrix.

Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix.



Problem Constraints

1 <= N, M <= 1000

0 <= A[i][j] <= 1



Input Format

The first argument given is the integer matrix A.



Output Format

Return the matrix B.



Example Input

Input 1:

 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1] 
       [0, 1, 1, 0]
     ]

Input 2:

 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]  
     ]



Example Output

Output 1:

 [ 
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]   
 ]

Output 2:

 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4] 
 ]



Example Explanation

Explanation 1:

 A[0][0], A[0][1], A[0][2] will be nearest to A[0][3].
 A[1][0], A[1][1] will be nearest to A[1][2].
 A[2][0] will be nearest to A[2][1] and A[2][3] will be nearest to A[2][2].

Explanation 2:

 There is only a single 1. Fill the distance from that 1.


"""
"""
Hint 1

Initially consider the nearest distance from 1 for all cells as infinity.
Now for each cell do a bfs and update the distance matrix accordingly.
This approach can lead to the correct answer but may caue a worst case complexity of O(N^2 * M^2).
Can we do better ?

"""
"""
Solution Approach

The idea is to use multi-source BFS. At the begining insert all the nodes having value 1 in the queue.

We first explore immediate adjacent of all 1’s, then adjacent of adjacent, and so on.

Only if the distance at the cell of matrix is greater than the current distance, then only we update the distance of the cell.

Therefore we find minimum distance.

Time Complexity: O( N x M)

"""

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        
        from collections import deque

        dq = deque([])
        row = len(A)
        col = len(A[0]) 
        
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    A[i][j] = 0
                    dq.append([i,j,0])
                else:
                    A[i][j] = -1
                    
        while dq:
            rowi, coli , dist = dq.popleft()
            # print(rowi, coli)
            # A[rowi][coli] = min(dist, A[rowi][coli])

            if rowi != 0 and A[rowi-1][coli] ==-1:
                dq.append([rowi-1, coli, dist+1])
                A[rowi-1][coli] = dist+1                

            if rowi < row-1 and A[rowi+1][coli] == -1:
                dq.append([rowi+1, coli, dist+1])
                A[rowi+1][coli] = dist+1 

            if coli != 0 and A[rowi][coli-1] == -1:
                dq.append([rowi, coli-1, dist+1])
                A[rowi][coli-1] = dist+1 

            if coli < col-1 and A[rowi][coli+1] == -1:
                dq.append( [rowi, coli+1, dist+1] )
                A[rowi][coli+1] = dist+1
         
        
        return A