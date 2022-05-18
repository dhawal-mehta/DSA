"""
Minimum number of deletions and insertions.


Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.

Example 1:

Input: str1 = "heap", str2 = "pea"
Output: 3
Explanation: 2 deletions and 1 insertion
p and h deleted from heap. Then, p is 
inserted at the beginning One thing to 
note, though p was required yet it was 
removed/deleted first from its position 
and then it is inserted to some other 
position. Thus, p contributes one to the 
deletion_count and one to the 
insertion_count.

Example 2:

Input : str1 = "geeksforgeeks"
str2 = "geeks"
Output: 8
Explanation: 8 deletions

 

Your Task:
You don't need to read or print anything. Your task is to complete the function minOperations() which takes both strings as input parameter and returns the minimum number of operation required.

Expected Time Complexity: O(|str1|*|str2|)
Expected Space Complexity: O(|str1|*|str2|)

Constraints:
1 ≤ |str1|, |str2| ≤ 1000
All the characters are lower case English alphabets
"""
"""
Hint 1
-->str1 and str2 be the given strings.
-->m and n be their lengths respectively.
-->len be the length of the longest 
   common subsequence of str1 and str2
-->// minimum number of deletions 
   minDel = m - len
-->// minimum number of Insertions 
   minInsert = n - len
"""

#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# code here
		X = s1
		Y = s2
		n = len(s1)
		m = len(s2)
		
		t = [[0]*(m+1) for i in range(n+1) ]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if X[i-1] == Y[j-1]:
                    t[i][j] = t[i-1][j-1]+1
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        return n+m - 2*t[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends