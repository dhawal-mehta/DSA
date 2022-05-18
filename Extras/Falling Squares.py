"""Falling Squares

Problem Description

On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (A[i] = (left, side_length)) is a square with the left-most point being A[i][0] and side length A[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.

Given A, find and return a list of heights H. Each height H[i] represents the current highest height of any square we have dropped, after dropping squares represented by A[0], A[1], ..., A[i].



Problem Constraints

1 <= length of the array A <= 1000
1 <= A[i][0] <= 108
1 <= A[i][1] <= 106


Input Format

The only argument given is the integer matrix A.


Output Format

Return an integer array H.


Example Input

Input 1:

 A = [ [1, 2], 
       [2, 3], 
       [6, 1] ]

Input 2:

 A = [ [100, 100], 
       [200, 100] ]



Example Output

Output 1:

 [2, 5, 5]

Output 2:

 [100, 100]



Example Explanation

Explanation 1:

Explanation 2:"""



class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        height = [0]*len(A)

        for i in range(0,len(A)):
            currStart = A[i][0]
            currLen = A[i][1]
            currEnd = currStart + currLen
            height[i] += currLen
            for j in range(i+1, len(A)):
                jStart = A[j][0]
                jLen = A[j][1]
                jEnd = jStart + jLen
                
                if currStart>=jEnd or currEnd<=jStart:
                    continue
                
                height[j] = max(height[j] , height[i])
        
        res = []
        currMaxHt = 0

        for i in height:
            currMaxHt = max(currMaxHt, i)
            res.append(currMaxHt)
        
        return res