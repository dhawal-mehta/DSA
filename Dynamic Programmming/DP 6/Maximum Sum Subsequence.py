"""Maximum Sum Subsequence

Problem Description

You are given an integer array A of size N.

Find the maximum sum of a subsequence of A such that no digit is repeated in subsequence.

You are allowed to use an integer if it contain multiple digit but you cannot use 2 different integer with same digit.

NOTE:

    A sequence S is subsequence of T if S can be generated by removing 0 or more elements from T.



Problem Constraints

1 <= N <= 1000

1 <= A[i] <= 109



Input Format

First and only argument of input contains an integer array A of size N.


Output Format

Return a single integer representing the maximum sum.


Example Input

Input 1:

 A = [25,15,16,99]

Input 2:

 A = [12,23,13]



Example Output

Output 1:

 140

Output 2:

 23



Example Explanation

Explanation 1:

  If we choose subsequence [25,16,99], there are no repeating digits and sum is maximized among all correct subsequences.

Explanation 2:

 Every pair of integer have a digit common. so, we can only choose 1 number.
"""
"""
Hint 1

can you somehow know which digits are used till now? how many digits are there?

Try to think of forming a bitmask for digits.

"""
"""
Solution Approach

Pre-Requisite: Dp Bitmask

Create a bit mask for all numbers.
For example: mask for number 1234 looks like 0000011110 (in binary system)
Performing dynamic programming with this mask will give us the answer.
Initialize dp with -1 and perform the following recurrence relation.

let dp(B,N) = max { dp(B^mask(A[i]),i) } for all i 0 to N-1

Time Complexity : O(N2)
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSum(self, A):
        
        def getBits(n):
            res = 0
            while n != 0:
                temp = n%10
                res |= 1<<temp
                n = n//10
            return res
        
        
        dp = [{} for i in A ]
        dpNum = {}
        
        res = max(A)
        
        for i in range(len(A)):
            temp = getBits(A[i])
            dp[i][temp] = A[i]
            dpNum[A[i]] = temp


        for i in range(1, len(A)):
            bitsi = dpNum[A[i]]
            
            for j in range(i-1, -1, -1):
                if dpNum[A[i]] & dpNum[A[j]] == 0:
                    
                    for currSeqBit in dp[j]:
                        if currSeqBit & bitsi == 0:
                            
                            if currSeqBit | bitsi in dp[i]:
                                dp[i][currSeqBit | bitsi] = max(dp[i][currSeqBit | bitsi], A[i]+dp[j][currSeqBit] )
                            else:
                                dp[i][currSeqBit | bitsi] =  A[i]+dp[j][currSeqBit]
                            
                            res = max(res, dp[i][currSeqBit | bitsi])
                            
        # for i in A:
        #     print(getBits(i))
        
        return res
        
                