"""
Odd Palindrome


Problem Description

A palindrome string is a string which reads the same forward and backward. If a palindrome string is of odd length l, then (l+1)/2th character (1 index based) is said to be the centre of the palindrome.

You are given a string A. Return an array X of integers where X[i] = (number of odd length palindrome subsequence of A with A[i] as the centre) modulo (109 + 7).

A subsequence of A is a string which can be derived from A by deleting some of its character.



Problem Constraints

1 <= length(A) <= 1000
Every character of A will be a lowercase English letter 'a' - 'z'.


Input Format

First and only argument is a string A.


Output Format

Return an integer array X as mentioned in the question.


Example Input

Input 1:

 A = "xyzx"

Input 2:

 A = "ababzz"



Example Output

Output 1:

 [1, 2, 2, 1]

Output 2:

 [1, 2, 2, 1, 1, 1]



Example Explanation

Explanation 1:

 
 Index(i)  |   Palindrome subsequences with centre i
   0       |   a        
   1       |   y, xyx
   2       |   z, xzx
   3       |   x
 So, output array is [1, 2, 2, 1]

Explanation 2:

 Index(i)  |  Palindrome subsequences with centre i
   0       |  a    
   1       |  b, aba
   2       |  a, bab
   3       |  b
   4       |  z
   5       |  z
 So, output array is [1, 2, 2, 1, 1, 1]  
 """
"""
Hint 1

For every i, we have to find the number of palindrome subsequences in left and right of i.
Think about using dynamic programming with states based on prefix and suffix.

"""
"""
Solution Approach

Let dp[i][j] represents the number of palindromic subsequences which are present in 0 to i - 1 and j to N - 1.

Let len be the distance between i and j. For each length len, we will fix our i and j, and check whether characters str[i] and str[j] are equal or not.Then according to it, we will make our dp transitions

If A[i] == A[j], then We can append the A[i] character to all the palindromic subsequences from 0 to i-1
Else there are no palindromic subsequences in 0 to i and j to n which contains both A[i] and A[j] caharacters.

dp[i][j] = dp[i-1][j] + dp[i][j+1] - dp[i-1][j+1] if A[i] != A[j]
dp[i][j] = dp[i-1][j] + dp[i][j+1 if A[i] == A[j]

Base Case: if i==0 and j==n-1, dp[i][j] = 2 if A[i] == A[j], else dp[i][j] = 1.

Now, dp[i-1][i+1] will give us the number of palindromic subsequences with centre i.

"""
class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
    
        n = len(A) 
    
        Mod = 1000000007
    
        # Created dp of size n+2 * n+2 so that, we don't have to check boundary conditions.
        dp=[[0 for i in range(n+2)] for i in range(n+2)]  
        
        for l in range(n+1, -1, -1):
            for i in range(0, n+2-l):
                j = i+l
            
                # base condtition, Number of ways to choose palindromic subsequence without any character on left or right is 1.
                if(i==0 or j == n+1):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j+1]
                    
                    # subtract dp[i-1][j+1], As dp[i-1][j] contains dp[i-1][j+1] and dp[i][j+1] contains dp[i-1][j+1] 
                    if(A[i-1] != A[j-1]):
                        dp[i][j] -= dp[i-1][j+1]
                
                dp[i][j] = (dp[i][j] + Mod) % Mod
    
        ans = []
    
        for i in range(1, n+1):
            if(i==1 or i==n):
                ans.append(1)
            else:
                ans.append(dp[i-1][i+1])
        
        return ans;
