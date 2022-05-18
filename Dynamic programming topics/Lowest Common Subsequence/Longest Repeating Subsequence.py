""""Longest Repeating Subsequence

Given a string str, find the length of the longest repeating subsequence such that it can be found twice in the given string. The two identified subsequences A and B can use the same ith character from string str if and only if that ith character has different indices in A and B.

Example 1:

Input:
str = "axxxy"
Output: 2
Explanation:
The given array with indexes looks like
a x x x y 
0 1 2 3 4

The longest subsequence is "xx". 
It appears twice as explained below.

subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str 


subsequence B
x x
0 1  <-- index of subsequence B
------
2 3  <-- index of str 

We are able to use character 'x' 
(at index 2 in str) in both subsequences
as it appears on index 1 in subsequence A 
and index 0 in subsequence B.

Example 2:

Input:
str = "aab"
Output: 1
Explanation: 
The longest reapting subsequenece is "a".


Your Task:
You don't need to read or print anything. Your task is to complete the LongestRepeatingSubsequence() which takes str as input parameter and returns the length of the longest repeating subsequnece.


Expected Time Complexity: O(n2)
Expected Space Complexity: O(n2)


Constraints:
1 <= |str| <= 103"""
"""
Hint 1

Use LCS.
"""

#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code 

		X = str
		Y = str
		n = len(str)
		m = n
		
		t = [[0]*(m+1) for i in range(n+1) ]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if X[i-1] == Y[j-1] and i!=j:
                    t[i][j] = t[i-1][j-1]+1
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        return t[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends