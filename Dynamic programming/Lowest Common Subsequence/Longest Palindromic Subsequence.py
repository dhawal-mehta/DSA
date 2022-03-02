"""
Longest Palindromic Subsequence

Given a String, find the longest palindromic subsequence.


Example 1:

Input:
S = "bbabcbcab"
Output: 7
Explanation: Subsequence "babcbab" is the
longest subsequence which is also a palindrome.

Example 2:

Input: 
S = "abcd"
Output: 1
Explanation: "a", "b", "c" and "d" are
palindromic and all have a length 1.


Your Task:
You don't need to read input or print anything. Your task is to complete the function longestPalinSubseq() which takes the string S as input and returns an integer denoting the length of the longest palindromic subsequence of S.


Expected Time Complexity: O(|S|*|S|).
Expected Auxiliary Space: O(|S|*|S|).


Constraints:
1 ≤ |S| ≤ 1000
"""
"""
Hint 1
A Palindrome reads same from the front and back.

Hence, longest palindromic subsequence is nothing but the longest common subsequence in S and reverse (S).
"""
        

#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        
        X = S
        Y = S[::-1]
        n = len(S)
        m= len(S)
        
        t = [[0]*(m+1) for i in range(n+1) ]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if X[i-1] == Y[j-1]:
                    t[i][j] = t[i-1][j-1]+1
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        return t[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends