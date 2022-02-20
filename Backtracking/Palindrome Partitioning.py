"""
Palindrome Partitioning


Problem Description

Given a string A, partition A such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of A.

Ordering the results in the answer : Entry i will come before Entry j if :

    len(Entryi[0]) < len(Entryj[0]) OR
    (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
    (len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))



Problem Constraints

1 <= len(A) <= 15


Input Format

First argument is a string A of lowercase characters.


Output Format

Return a list of all possible palindrome partitioning of s.


Example Input

Input 1:

A = "aab"

Input 2:

A = "a"



Example Output

Output 1:

 [
    ["a","a","b"]
    ["aa","b"],
  ]

Output 2:

 [
    ["a"]
  ]



Example Explanation

Explanation 1:

In the given example, ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa").

Explanation 2:

In the given example, only partition possible is "a" ."""
"""
Hint 1

Since, we are listing out all the partitions ( and not counting them), we need to do brute force here.

Think of recursion.
"""
"""
Solution Approach

We can use recursion to generate all possible palindrome partitioning of s.

When on index i, you incrementally check all substring starting from i for being palindromic. If found, you recursively solve the problem for the remaining string and add it to your solution. Start this recursion from starting position of the string.

PS: You can optimize your solution by not computing the answer for same index multiple times using Dynamic Programming.
"""
class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
    	result = []
    	self.partition_2(result, [], A, 0)
    	return result
    def partition_2(self, result, cur, A, i):
    	if i == len(A):
    		result.append(list(cur))
    	for j in range(i, len(A)):
    		if self.isPalindrome(A[i:j+1]):
    			cur.append(A[i:j+1])
    			self.partition_2(result, cur, A, j+1)
    			cur.pop()
    def isPalindrome(self, A):
    	return list(A) == list(reversed(A))

