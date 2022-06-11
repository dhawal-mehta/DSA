"""
Longest Common Subsequence

Problem Description

Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.



Problem Constraints

1 <= Length of A, B <= 1005



Input Format

First argument is a string A.
Second argument is a string B.



Output Format

Return an integer denoting the length of the longest common subsequence.



Example Input

Input 1:

 A = "abbcdgf"
 B = "bbadcgf"

Input 2:

 A = "aaaaaa"
 B = "ababab"



Example Output

Output 1:

 5

Output 2:

 3



Example Explanation

Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5.

Explanation 2:

 The longest common subsequence is "aaa", which has a length of 3."""

 
"""
Hint 1

If for some (i, j) A[i] = B[j], then we can break our problem:

Longest commen subsequence of(A[1..i-1], B[1….j-1]) + 1(for A[i] == B[j]) + Longest commen subsequence of(A[i+1….n], B[j+1….m]).

To find the longest common subsequence of given strings, Do this for all i, j.

Try to reduce the time complexity of this solution ?

"""
"""
Solution Approach

Suppose LCS[i][j] represents the longest common subsequence of A[1..i] and B[1..j]

A[1..i] represents first i characters of string A
A[1..j] represents first j characters of string B

For every i, j we have two conditions A[i] == B[j] or not. Divide the problem based on this condition.

Recursion relation to divide the problem into smaller sub problems can be written as:-

LCS(i, j) = maximum (LCS(i-1, j-1] + 1,       //if(A[i] = B[j])
                     LCS(A[i-1], B[j],
                     LCS(A[i], B[j-1] )

LCS[ len(A) ][ len(B) ] will be our answer.

Think about the time complexity of this solution.

"""
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        dp = [[0 for i in A] for j in B]
        
        for i in range(0, len(A)):
            if A[i]==B[0]:
                dp[0][i] = 1
            elif i > 0:
                dp[0][i] = dp[0][i-1]
        
        for i in range(0, len(B)):
            if B[i] == A[0]:
                dp[i][0] = 1
            elif i>0:
                dp[i][0] = dp[i-1][0]
        
        for i in range(1, len(B)):
            for j in range(1, len(A)):
                if B[i] == A[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]