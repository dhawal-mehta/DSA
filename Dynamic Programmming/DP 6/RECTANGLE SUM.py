"""RECTANGLE SUM


Problem Description

Given a matrix of integers A of size N x M.

Calculate the sum of all submatrices and return the maximum among all those sums.

NOTE: Empty submatrix also need to be considered.



Problem Constraints

1 <= N, M <= 100
-10000 <= A[i] <= 10000



Input Format

The first and only argument given is the integer matrix A.



Output Format

Return the maximum sum among all those sums of all possible submatrices.



Example Input

Input 1:

 A = [
       [1, 3, -2]
       [1, 4, 6]
       [-4, -2, 1] 
     ]

Input 2:

 
A = [  
      [-1, -1]
      [-1, -1] 
    ]



Example Output

Output 1:

 13

Output 2:

 0



Example Explanation

Explanation 1:

 Submatrix giving maximum sum is : 
    [ 
       [1, 3, -2]
       [1, 4, 6]
    ]

Explanation 2:

 Sum of empty submatrix will be 0.
 """
"""
 Hint 1

Try fixing the left and right coloumn of the submatrix.

Now, Can you apply kadane(Maximum-Sum subarray) algorithm to find the maximum sum?

"""
"""
character backgroundcharacter
Solution Approach

Naive solution is to check every possible rectangle in given 2D array.
The time complexity of this solution would be O(n^4).

Let’s optimize it.

The idea is to use Kadane’s algorithm(to find maximum sum subarray) and Fix the left and right columns.

For each pair of (left, right) coloumn, we basically find top and bottom row numbers such that the submatrix have maximum sum.

To find the top and bottom row numbers, calculate sum of elements in every row from left to right and store these sums in an array say temp[].
So temp[i] indicates sum of elements from left to right in row i. If we apply Kadane’s 1D algorithm on temp[], and get the maximum sum subarray of temp, this maximum sum would be the maximum possible sum with left and right as boundary columns.

To get the overall maximum sum, we compare this sum with the maximum sum so far.

"""
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        # res_ = float("-inf")
        
        # for i in range(len(A)):
        #     for j in range(1, len(A[0])):
        #         A[i][j] += A[i][j-1]
                
        # for j in range(len(A[0])):
        #     for i in range(1, len(A) ):
        #         A[i][j] += A[i-1][j]
        # # print(A)
        
        # for topx in range(0, len(A)):
        #     for topy in range(0, len(A[0])):
        #         for botx  in range(topx , len(A)):
        #             for boty in range(topy, len(A[0])):
        #                 temp = A[botx][boty]
        #                 temp -= A[topx -1][boty] if topx > 0 else 0
        #                 temp -= A[botx][topy-1] if topy >0 else 0
        #                 temp += A[topx -1][topy-1] if topx > 0 and topy > 0 else 0
                        
        #                 res_ = max(res_, temp)
        
        # return 0 if res_ <=0 else res_
        
        res = float('-inf')
        
        # temp = [0 for i in range(len(A[0])) ]
        
        def getKadane(arr):
            if len(arr) == 0:
                return 0
                
            start = -1
            end = 0
            
            res = float('-inf')
            currSum = 0
            temp = 0

            
            while end < len(arr):
                if arr[end] >= 0:
                    if start == -1:
                        start = end
                    
                    currSum += arr[end]
                    end += 1
                else:
                    if currSum + arr[end] > 0:
                        currSum += arr[end]
                        end+=1
                    else:
                        if start+1 == end:
                            currSum = 0
                            start = -1
                            end += 1
                        else:
                            if start >= 0:
                                currSum -= arr[start]
                                start += 1
                            else:
                                end += 1

                        
                res = max(res, currSum)
            
            return 0 if res < 0  else res
        
        # print(getKadane([-5 , 7, -6, 6]))
        
        for c1 in range(0, len(A[0])):
            temp = [0 for i in range(len(A)) ]
            for c2 in range(c1, len(A[0])):
                
                for r in range(len(A)):
                    temp[r] += A[r][c2]
                
                res = max(res, getKadane(temp))
        
        return res
                    
                    
                
            
       