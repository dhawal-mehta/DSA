"""
Max Rectangle in Binary Matrix


Problem Description

Given a 2-D binary matrix A of size N x M filled with 0's and 1's, find the largest rectangle containing only ones and return its area.



Problem Constraints

1 <= N, M <= 100



Input Format

The first argument is a 2-D binary array A.



Output Format

Return an integer denoting the area of the largest rectangle containing only ones.



Example Input

Input 1:

 A = [
       [1, 1, 1]
       [0, 1, 1]
       [1, 0, 0] 
     ]

Input 2:

 A = [
       [0, 1, 0]
       [1, 1, 1]
     ] 



Example Output

Output 1:

 4

Output 2:

 3



Example Explanation

Explanation 1:

 As the max area rectangle is created by the 2x2 rectangle created by (0, 1), (0, 2), (1, 1) and (1, 2).

Explanation 2:

 As the max area rectangle is created by the 1x3 rectangle created by (1, 0), (1, 1) and (1, 2).
"""
"""
Hint 1

The brute-force approach is to look at all pairs of (i, j) to (k, l) and check if it’s filled with 1s. This approach, however, is O(NNNNN^2) = O(N^6). [ N^4 ways to choose i,j,k,l, and then N^2 elements in the square ].
Can you optimize this approach if you had additional space to store results for your previous calculations?
Maybe if you knew the result for (i, j) to (k, l - 1) or (i, j) to (k - 1, l) or both?

"""
"""
Hint 2

We can improve from N^6 by storing in dp[i][j][k][l] if (i,j) to (k,l) is all filled with 1.
dp[i][j[k][l] = 1 iff dp[i][j][k][l-1] = 1 && dp[i][j][k-1][l] = 1 and matrix[k][l] = 1.

Now we can improve this further. What if with every (i,j) we stored the length of 1s in the same row i starting from (i,j).
Can we move down in the column j from row i and determine the largest rectangle without visiting all cells ?

"""
"""
character
Solution Approach

Lets max_x[i][j] denote the length of 1s in the same row i starting from (i,j).

So our current max with one end of the rectangle at (i,j) would be max_x[i][j].
As we move to the next row, there are 2 cases :
1) max_x[i+1][j] >= max_x[i][j] which means that we can take max_x[i][j] 1s from next column as well and extend our current rectangle as it is, with one more extra row.
11100000 - 111
11111100 - 111

2) max_x[i+1][j] < max_x[i][j] which means that if we want to extend our current rectangle to next row, we need to reduce the number of columns in it to max_x[i+1][j]
11100000 - 11
11000000 - 11

As mentioned above, we keep increasing the columns and adjusting the rectangle’s width.
O(N^3) time complexity.

Even though N^3 is acceptable, it might be worth exploring a better solution.
If you notice, laying out max_x[i][j] helps you make histograms in every row. Then the problem becomes of finding the maximum area in histograms ( which we have solved before in Stacks and Queues ) in O(n). This would lead to an O(N^2) solution. We strongly suggest you explore the O(N^2) solution as well.

"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        
        for i in range(0, len(A)):
            curr = 0
            for j in range(len(A[0])-1, -1, -1):
                if A[i][j] == 1:
                    A[i][j] = curr + 1
                    curr += 1
                else:
                    curr = 0
        # print(A)
        
        maxArea = float('-inf')
        for i in range(len(A)):
            for j in range(len(A[0])):
                
                if A[i][j] > 0:
                    
                    k = i
                    row = 0
                    col = A[i][j]
                    
                    currArea = float('-inf')
                    while k < len(A):
                        # print(k)
                        if A[k][j] == 0:
                            break
                        
                        row += 1
                        col = min(col, A[k][j])
                        currArea = max(currArea, row*col)
                        k+=1
                        
                    # print(i,j, currArea)
                    
                    maxArea = max(currArea, maxArea)
                
        return maxArea if maxArea > 0 else 0
