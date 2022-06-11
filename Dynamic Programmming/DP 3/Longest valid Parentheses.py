"""
Longest valid Parentheses


Problem Description

Given a string A containing just the characters '(' and ')'.

Find the length of the longest valid (well-formed) parentheses substring.



Problem Constraints

1 <= length(A) <= 750000



Input Format

The only argument given is string A.



Output Format

Return the length of the longest valid (well-formed) parentheses substring.



Example Input

Input 1:

 A = "(()"

Input 2:

 A = ")()())"



Example Output

Output 1:

 2

Output 2:

 4



Example Explanation

Explanation 1:

 The longest valid parentheses substring is "()", which has length = 2.

Explanation 2:

 The longest valid parentheses substring is "()()", which has length = 4.
"""
"""
Hint 1

If you know the longest parenthesis ending at index i, can you use that to compute answer?

Try to simulate using stack and DP.

"""
"""
Solution Approach

Lets construct longest[i] where longest[i] denotes the longest set of parenthesis ending at index i.

    If s[i] is ‘(‘, set longest[i] to 0, because any string end with ‘(‘ cannot be a valid one.
    Else if s[i] is ‘)’
    If s[i-1] is ‘(‘, longest[i] = longest[i-2] + 2
    Else if s[i-1] is ‘)’ and s[i-longest[i-1]-1] == ‘(‘, longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

"""
class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        # stk = []
        # maxl = 0
        
        # for i in range(0, len(A)):
        #     if A[i] == '(':
        #         stk.append(i)
        #     elif A[i] == ')' and len(stk) > 0 and A[stk[-1]] =='(':
        #         stk.pop()
        #         temp =  stk[-1] if len(stk) > 0 else -1
        #         maxl = max(maxl, i-temp)
        #     else:
        #         if len(stk) > 0 and A[stk[-1]] == ')':
        #             stk.pop()
                    
        #         stk.append(i)
            
        # return maxl

        maxl =0
        left = 0 
        right = 0
        for i in range(0, len(A)):
            if A[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                maxl = max(2*left, maxl)
            
            if right > left:
                right = 0
                left = 0

        left = 0 
        right = 0
        for i in range(len(A)-1, -1,-1):
            if A[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                maxl = max(2*left, maxl)
            
            if right < left:
                right = 0
                left = 0        
        
        return maxl
        
        
        
        