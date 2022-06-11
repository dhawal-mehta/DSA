"""
Longest Palindromic Subsequence


Problem Description

Given a string A. Find the longest palindromic subsequence (A subsequence which does not need to be contiguous and is a palindrome).

You need to return the length of longest palindromic subsequence.



Problem Constraints

1 <= length of(A) <= 103



Input Format

First and only integer is a string A.



Output Format

Return an integer denoting the length of longest palindromic subsequence.



Example Input

Input 1:

 A = "bebeeed"

Input 2:

 A = "aedsead"



Example Output

Output 1:

 4

Output 2:

 5



Example Explanation

Explanation 1:

 The longest palindromic subsequence is "eeee", which has a length of 4.

Explanation 2:

 The longest palindromic subsequence is "aedea", which has a length of 5.

"""
"""
Hint 1

Naive solution is to generate all the possible subsequences and check the longest palindromic subsequence.
But this will take exponential time.

Can you optimize it using Dynamic Programming?

"""
"""
Solution Approach

First, Create a recurrence relation then we will think of optimizing that.
Let’s say for sequence A[0..n-1] , L(0,n-1) denotes the length of longest palidromic subsequence.
It will be calculated by:
-> If last and first character of the sequence are same, then L(0,n-1) = L(1,n-1) + 2
->Else, L(0,n-1) = max(L(0,n-2),L(1,n-1))

Since we can observe overlapping Subproblems, we will optimize it using a dynamic programming solution.

"""
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        dp = [[0 for i in A] for j in A]
        
        for l in range(1, len(A)+1):
            for end in range(l-1, len(A)):
                start = end - l + 1
                if l <= 2:
                    if A[start] == A[end]:
                        dp[start][end] = l
                else:
                    if A[start] == A[end]:
                        dp[start][end] = dp[start+1][end-1] + 2
                    else:
                        dp[start][end] = max(dp[start+1][end], dp[start][end-1])
        # print(dp)
        return dp[0][-1]