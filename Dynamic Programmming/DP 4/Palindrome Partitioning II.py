"""Palindrome Partitioning II


Problem Description

Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.



Problem Constraints

1 <= length(A) <= 501



Input Format

The first and the only argument contains the string A.



Output Format

Return an integer, representing the minimum cuts needed.



Example Input

Input 1:

 A = "aba"

Input 2:

 A = "aab"



Example Output

Output 1:

 0

Output 2:

 1



Example Explanation

Explanation 1:

 "aba" is already a palindrome, so no cuts are needed.

Explanation 2:

 Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
"""
Hint 1

You can try to see, the problem has overlapping subproblems and optimal substructure,
so you can try to think in terms of DP. Make the overlapping subproblems and optimal substructure
as your dp states and think about transitions.

"""

"""
Solution Approach

Firstly, we should be able to answer if substring [i,i+1,….j] is palindrome or not in O(1)
with pre-computation of O(n^2).

Now try to come up with some DP state which can find minimum cut using above data.
Transitions should also be thought of carefully. They should relate the answer of a previously
computed subproblem and use it to form new answer.

"""
class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        isPalindrome = [ [0 for i in range(len(A))] for j in range(len(A)) ]
        
        for l in range(0, len(A)):
            for end in range(l  , len(A)):
                start = end - l
        
                if start == end:
                    isPalindrome[start][end] = 1
                elif start + 1 == end:
                    if A[start] == A[end]: 
                        isPalindrome[start][end] = 1
                else:
                    if A[start] == A[end] and isPalindrome[start+1][end-1] == 1:
                        isPalindrome[start][end] = 1
        
        # for i in range(0, len(A)):
        #     for j in range(0,len(A)):
        #         if isPalindrome[i][j] == 1:
        #             print(i,j)
        #             if i != j:
        #                 print(A[i:j+1])
        
        cuts = [ i for i in range(len(A)) ]
        
        for i in range(len(A)):
            for j in range(0, i+1):
                
                if isPalindrome[j][i] == 1 and j==0:
                    cuts[i] = 0
                    
                if isPalindrome[j][i] == 1 and j!= 0:
                    cuts[i] = min(cuts[i], cuts[j-1]+1)

        return cuts[-1]