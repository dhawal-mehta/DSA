"""
Longest Common Substring

Given two strings. The task is to find the length of the longest common substring.


Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR"
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.

Example 2:

Input: S1 = "ABC", S2 "ACB"
Output: 1
Explanation: The longest common substrings
are "A", "B", "C" all having length 1.


Your Task:
You don't need to read input or print anything. Your task is to complete the function longestCommonSubstr() which takes the string S1, string S2 and their length n and m as inputs and returns the length of the longest common substring in S1 and S2.


Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).


Constraints:
1<=n, m<=1000
"""
#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        t = [ [0]*(m+1) for i in range(n+1) ]
        
        res = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    t[i][j] = t[i-1][j-1] + 1
                    res = max( t[i][j], res)
                else:
                    t[i][j] = 0
        
        return res
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends
