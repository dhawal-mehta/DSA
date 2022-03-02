"""
Shortest Common Supersequence

Given two strings X and Y of lengths m and n respectively, find the length of the smallest string which has both, X and Y as its sub-sequences.
Note: X and Y can have both uppercase and lowercase letters.

Example 1

Input:
X = abcd, Y = xycd
Output: 6
Explanation: Shortest Common Supersequence
would be abxycd which is of length 6 and
has both the strings as its subsequences.

Example 2

Input:
X = efgh, Y = jghi
Output: 6
Explanation: Shortest Common Supersequence
would be ejfghi which is of length 6 and
has both the strings as its subsequences.

Your Task:
Complete shortestCommonSupersequence() function that takes X, Y, m, and n as arguments and returns the length of the required string.

Expected Time Complexity: O(Length(X) * Length(Y)).
Expected Auxiliary Space: O(Length(X) * Length(Y)).

Constraints:
1<= |X|, |Y| <= 100
"""
"""
Hint 1

1. Use dp[][] array to store length of shortest common supersequence.

2. dp[i][j] contains length of shortest common supersequence of X[0..i-1] and Y[0..j-1].

3. Iterate over both strings using nested loop.

4. For each iteration:

    i is 0, dp[i][j] will be equal to size of second string else if j is 0, dp[i][j] will be equal to size of first string.
    If character of both strings are same then dp[i][j] will be 1+ dp[i-1][j-1].
    Else dp[i][j] will be 1+ minimum answer without considering the current character of 2 strings.

5. Return the result.
"""

#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, n, m):
        
        t = [[0]*(m+1) for i in range(n+1) ]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if X[i-1] == Y[j-1]:
                    t[i][j] = t[i-1][j-1]+1
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        return n+m - t[-1][-1]
                
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends