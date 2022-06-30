"""
Repeating Subsequence


Problem Description

Given a string A, find if there is any subsequence that repeats itself.

A subsequence of a string is defined as a sequence of characters generated by deleting some characters in the string without changing the order of the remaining characters.

NOTE:
1. Subsequence length should be greater than or equal to 2.
2. The repeating subsequence should be disjoint that is in both the sequence no character in the same order and position should be taken from the same index of the original string.



Problem Constraints

1 <= length(A) <= 100



Input Format

The first and the only argument of input contains a string A.



Output Format

Return an integer, 1 if there is any subsequence which repeat itself else return 0.



Example Input

Input 1:

 A = "abab"

Input 2:

 A = "abba"



Example Output

Output 1:

 1

Output 2:

 0



Example Explanation

Explanation 1:

 "ab" is repeated.

Explanation 2:

 There is no repeating subsequence."""

"""
Hint 1

Our task is to find a repeating subsequence.
Or rather, lets say if we can find the longest repeating subsequence. If the length > 1, we return 0.

Now, to find longest repeating subsequence, lets try finding the longest common subsequence between the string A and itself ( LCS(A, A) ).
The only restriction we want to impose is that you cannot match a character with its replica in the other string.
In other words, if S1 and S2 are the replicas of the string for which we want to find LCS, S1[i] != S2[i] for all index i.

"""
"""
Solution Approach

Ok here we will see what is the recurrance relation for our problem

Rec(i, j) =   |
              |   Rec(i + 1, j)
         max  |
              |   Rec(i, j + 1)
              |
              |   Rec(i + 1, j + 1) + 1 IF i != j and A[i] == A[j] 
              |

We will leave it upto you to take care of the base cases

Happy Coding

"""
class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        dp = [ [0 for  i in range(len(A)+1)] for i in range(len(A)+1)]
        
        for i in range(1, len(A)+1):
            for j in range(1, len(A)+1):
                if A[i-1] == A[j-1] and i != j:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
                if dp[i][j] >=2 :
                    return 1
        
        # print(dp)
        
        return 0
        