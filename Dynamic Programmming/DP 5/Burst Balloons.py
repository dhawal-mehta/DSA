"""Burst Balloons


Problem Description

You are given N balloons each with a number of coins associated with them. An array of integers A represents the coins associated with the ith balloon.
You are asked to burst all the balloons. If the you burst balloon ith you will get A[left] * A[i] * A[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

NOTE: You may imagine A[-1] = A[N] = 1. They are not real therefore you can not burst them.



Problem Constraints

1 <= N <= 100
1 <= A[i] <= 100



Input Format

The only argument given is the integer array A.



Output Format

Return the maximum coins you can collect by bursting the balloons wisely.



Example Input

Input 1:

 A = [3, 1, 5, 8]

Input 2:

 A = [3, 1, 2]



Example Output

Output 1:

 167

Output 2:

 15



Example Explanation

Explanation 1:

 Burst ballon at index 1, coins collected = 3*1*5=15 , A becomes = [3, 5, 8] 
 Burst ballon at index 1, coins collected = 3*5*8=120 , A becomes = [3, 8]
 Burst ballon at index 0, coins collected = 1*3*8=24 , A becomes = [8]
 Burst ballon at index 0, coins collected = 1*8*1 = 8
 Total coins collected = 15 + 120 + 24 + 8 = 167

Explanation 2:

 Burst ballon at index 1, coins collected = 3*1*2 = 6, A becomes = [3, 2] 
 Burst ballon at index 1, coins collected = 3*2*1 = 6, A becomes = [3]
 Burst ballon at index 0, coins collected = 1*3*1 = 3
 Total coins collected = 6 + 6 + 3 = 15


"""
"""
Hint 1

In the first try, the obvious solution is to find every possible order in which balloons can be burst.
This lead to time complexity of O(N!). We can improve further by caching the set of existing balloons.
Since each balloon can be burst or not burst, and
we are incurring extra time creating a set of balloons each time, we are still looking at a solution worse than O(2^N).
Try to Think where we can apply dynamic programming here.

"""
"""
Solution Approach

We define a function dp to return the maximum number of coins obtainable on the open interval (left, right).
Our base case is if there are no integers on our interval (left + 1 == right), and
therefore there are no more balloons that can be added.
We add each balloon on the interval, divide and conquer the left and right sides, and find the maximum score.

The best score after adding the ith balloon is given by:
A[left] * A[i] * A[right] + dp(left, i) + dp(i, right)

A[left] * A[i] * A[right] is the number of coins obtained from adding the ith balloon, and dp(left, i) + dp(i, right) are the maximum number of coins obtained from solving the left and right sides of that balloon respectively.

"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # # import math
        # logger = {1:0}
        
        # curr = 1
        # while curr < 100:
        #     logger[2**curr] = curr
        #     curr += 1
        
        # # print(logger)
        
        # def util(origNum):
            
        #     if origNum in dp :
        #         return dp[origNum]
            
        #     left = -1
        #     res = float('-inf')
        #     num = origNum
        #     while(num > 0):
        #         curr = num&~(num-1)
        #         num -=  curr
        #         right = -1 if num == 0 else num&~(num-1)
                
        #         multValue = (1 if left == -1 else A[logger[left]] )*A[logger[curr]]*( 1 if right ==-1 else A[logger[right]] )

        #         res = max(res, multValue + util(origNum-curr))
                
        #         left = curr
            
        #     dp[origNum] = res
            
        #     return res
        
        # dp = {}
        # dp[0] = 0
        
        # return util( 2**len(A) - 1) 
        
        # ------------ TLE --------------------
            
            
        dp = [ [0 for i in range(len(A))] for j in range(len(A)) ]
        
        for size in range(1, len(A)+1):
            for end in range(size-1, len(A)):
                start = end - size + 1
                tempAns = float('-inf')
                
                for lastBursted in range(start, end+1):
                    left = 0 if lastBursted == start else dp[start][lastBursted-1]
                    multValue = ( 1 if start == 0 else A[start-1])*A[lastBursted]*(1 if end+1 == len(A) else A[end+1])
                    right = 0 if lastBursted == end else dp[lastBursted+1][end]
                    
                    tempAns = max(tempAns, left+multValue+right)
                
                dp[start][end] = tempAns
        
        return dp[0][-1]
                
                