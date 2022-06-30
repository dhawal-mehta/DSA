"""Length of Longest Fibonacci Subsequence

Problem Description

Given a strictly increasing array A of positive integers forming a sequence.

A sequence X1, X2, X3, ..., XN is fibonacci like if

N > =3
Xi + Xi+1 = Xi+2 for all i+2 <= N

Find and return the length of the longest Fibonacci-like subsequence of A.

If one does not exist, return 0.

NOTE: A subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.



Problem Constraints

3 <= length of the array <= 1000

1 <= A[i] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return the length of the longest Fibonacci-like subsequence of A.
If one does not exist, return 0.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5, 6, 7, 8]

Input 2:

 A = [1, 3, 7, 11, 12, 14, 18]



Example Output

Output 1:

 5

Output 2:

 3



Example Explanation

Explanation 1:

 The longest subsequence that is fibonacci-like: [1, 2, 3, 5, 8].

Explanation 2:

 The longest subsequence that is fibonacci-like: [1, 11, 12], [3, 11, 14] or [7, 11, 18].
 The length will be 3."""

"""
Hint 1

Take two terms and find the next expected term, Move unitl next expected term is not found.

"""
"""
Solution Approach

Think of two consecutive terms A[i], A[j] in a fibonacci-like subsequence as a single node (i, j), and the entire subsequence is a path between these consecutive nodes. For example, with the fibonacci-like subsequence (A[1] = 2, A[2] = 3, A[4] = 5, A[7] = 8, A[10] = 13), we have the path between nodes (1, 2) <-> (2, 4) <-> (4, 7) <-> (7, 10).

The motivation for this is that two nodes (i, j) and (j, k) are connected if and only if A[i] + A[j] == A[k], and we needed this amount of information to know about this connection. Now we have a problem similar to Longest Increasing Subsequence.

Let longest[i, j] be the longest path ending in [i, j]. Then longest[j, k] = longest[i, j] + 1 if (i, j) and (j, k) are connected. Since i is uniquely determined as A.index(A[k] - A[j]), this is efficient: we check for each j < k what i is potentially, and update longest[j, k] accordingly.

Time Complexity: O(N^2) where N is the length of A.

"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        dp = [ {} for i in range(len(A)) ]
        
        maxLength = 2
        
        for i in range(1, len(A)):
            for j in range(0,i):
                
                dp[i][A[i] + A[j]] = 3
                
        for end in range(2, len(A)):
            for last in range(1, end):
                if A[end] in dp[last]:
                    maxLength = max(maxLength, dp[last][A[end]] )
                    
                    if A[last] + A[end] in dp[end]:
                        dp[end][A[end] + A[last]] = max(dp[end][A[last] + A[end]], dp[last][A[end]] +1)
                    else:
                        dp[end][A[end] + A[last]]  = dp[last][A[end]] + 1
                    
                    dp[last].pop(A[end])
                
        
        return maxLength