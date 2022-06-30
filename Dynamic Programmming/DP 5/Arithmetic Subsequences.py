"""Arithmetic Subsequences


Problem Description

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

 1, 3, 5, 7, 9
 7, 7, 7, 7

Given an integer array A of size N. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk](0-based indexing) is arithmetic. In particular, this means that k ≥ 2.

Return the number of arithmetic subsequences slices in the array A.



Problem Constraints

1 <= N <= 1000

-105 <= A[i] <= 105



Input Format

The first and the only argument of input contains an integer array, A of size N.



Output Format

Return an integer representing the number of arithmetic subsequences in A.



Example Input

Input 1:

 A = [2, 4, 6, 8, 10]

Input 2:

 A = [3, 6, 7]



Example Output

Output 1:

 7

Output 2:

 0



Example Explanation

Explanation 1:

 All arithmetic subsequence slices are:
    [2, 4, 6]
    [4, 6, 8]
    [6, 8, 10]
    [2, 4, 6, 8]
    [4, 6, 8, 10]
    [2, 4, 6, 8, 10]
    [2, 6, 10]

Explanation 2:

 There are no possible arithmetic subseqence.


"""
"""
Hint 1

Naive approach is to genereate all the subsequences and of length greater than 2. But this will take exponential time.

Think of using dynamic Programming using the fact we need atleast two parameter to determine an Arithmetic sequence i.e. first or last element and common difference.

"""
"""
Solution Approach

We need at least two parameter: last element and common difference.

Let’s say we denote dp[i][dif] denotes the number of arithmetic sequence that ends at A[i] and have common difference dif.

Now the state transitions are quite straightforward:

-> for all j < i, dp[i][A[i] - A[j]] += (dp[j][A[i] - A[j]] + 1).

Note that we will only add the arithmetic sequence which have length greater than 2. For that we can maintain an auxillary res variable and update that accordingly.

"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        dp = [ {} for i in range(len(A)) ]
        
        res = 0
        for  i in range(1, len(A)):
            for j in range(i-1, -1, -1):
                if A[i] - A[j]  in dp[j]:
                    if A[i] - A[j] in dp[i]:
                        dp[i][A[i]-A[j]] += dp[j][A[i]-A[j]] + 1
                    else:
                        dp[i][A[i]-A[j]] += 1
                        
                    res += dp[j][A[i]-A[j]] + 1
                else:
                    if A[i] - A[j] in dp[i]:
                        dp[i][A[i]-A[j]] += 1
                    else:
                        dp[i][A[i]-A[j]] = 1
                    
                    res += 1
        
        return res - (len(A)*(len(A) - 1))//2
                