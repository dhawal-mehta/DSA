"""Russian Doll Envelopes


Problem Description

Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.

One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

Find the maximum number of envelopes you can put one inside other.



Problem Constraints

1 <= N <= 1000
1 <= A[i][0], A[i][1] <= 109


Input Format

The only argument given is the integer matrix A.


Output Format

Return an integer denoting the maximum number of envelopes you can put one inside other.


Example Input

Input 1:

 A = [ 
         [5, 4]
         [6, 4]
         [6, 7]
         [2, 3]  
     ]

Input 2:

 A = [     '
         [8, 9]
         [8, 18]    
     ]



Example Output

Output 1:

 3

Output 2:

 1



Example Explanation

Explanation 1:

 Step 1: put [2, 3] inside [5, 4]
 Step 2: put [5, 4] inside [6, 7]
 3 envelopes can be put one inside other.

Explanation 2:

 No envelopes can be put inside any other so answer is 1.
"""
"""
Hint 1

Think of finding longest longest increasing subsequence in 2-dimensional.
"""
"""
Solution Approach

This is the same question as longest increase sub sequance.
The only problem is how to trasnform this problem to it.
We just sort the envelopes by width, but when there are even case( two envelope with the same width) we should put the height in reverse order.
like (5,6), (5,8), we should put (5,8) before (5,6).

Now the problem reduces to finding the longest increasing subsequence.

"""
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        # dp = {}
        # for w,h in A:
        #     dp[(w,h)] = 1
        
        # for i in range(1, len(A)):
        #     currMax = dp[ (A[i][0], A[i][1]) ]
        #     for j in range(0, i):
        #         if A[i][0] > A[j][0] and A[i][1] > A[j][1]:
        #             # and A[i][0] > A[j][1] and A[i][1] > A[j][0] 
        #             currMax = max(currMax, dp[(A[i][0], A[i][1])] + dp[(A[j][0],A[j][1])] )
                
        #         elif A[i][0] < A[j][0]  and A[i][1] < A[j][1]:
        #             # and A[i][0] < A[j][1] and A[i][1] < A[j][0]
        #             dp[(A[j][0], A[j][1])] = dp[(A[j][0], A[j][1])] + 1
                
        #         # print(i,j, dp)
        #     dp[(A[i][0], A[i][1])] = currMax
        
        # res = float('-inf')
        
        # # print(dp)
        
        # for i,j in A:
        #     res = max(res, dp[(i,j)])
        
        # return res
        
        #sorted as a pair
        
        X = [i[0] for i in A]
        Y = [i[1] for i in A]
        
        # print(X,Y)
        
        X, Y = zip(*sorted(zip(X, Y)))
        
        dp = {}
        
        for i in A:
            dp[(i[0], i[1])] = 1
        
        res = 1 if len(A) > 0 else 0
        
        for i in range(1, len(A)):
            for j in range(0, i):
                if X[i] > X[j] and Y[i] > Y[j]:
                    dp[(X[i], Y[i])] = max(dp[(X[i], Y[i])], dp[(X[j], Y[j])] + 1 )
            
            res = max(res, dp[(X[i],Y[i])])
        
        # print(dp)
        # print(res)
        # print(X,Y)
        
        return res
        
        