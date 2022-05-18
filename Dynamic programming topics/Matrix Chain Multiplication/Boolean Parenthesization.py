"""
Boolean Parenthesization


Given a boolean expression S of length N with following symbols.
Symbols
    'T' ---> true
    'F' ---> false
and following operators filled between symbols
Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

 

Example 1:

Input: N = 7
S = T|T&F^T
Output: 4
Explaination: The expression evaluates 
to true in 4 ways ((T|T)&(F^T)), 
(T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).

Example 2:

Input: N = 5
S = T^F|F
Output: 2
Explaination: ((T^F)|F) and (T^(F|F)) are the 
only ways.

 

Your Task:
You do not need to read input or print anything. Your task is to complete the function countWays() which takes N and S as input parameters and returns number of possible ways modulo 1003.

 

Expected Time Complexity: O(N3)
Expected Auxiliary Space: O(N2)

 

Constraints:
1 ≤ N ≤ 200 """
"""
Hint 1
For each segment find out how many ways are there to get T as result.
"""
"""
Hint 2
Use memoization to reduce time complexity.
"""
"""
Hint 3
Matrix chain multiplication problem can help you.
"""
#User function Template for python3

class Solution:
    def __init__(self):
        self.memo = {}
        
    def countWaysMemo(self, N, S, i, j):
        if i>j or j>N:
            return 0
            
        if i==j:
            return [1,0] if S[i] == 'T' else [0,1]
         
        if  (i,j) in self.memo:
            return self.memo[(i,j)]
        
        
        tempT = 0
        tempF = 0
        
        for k in range(i+1,j, 2):
            TrueL,FalseL = self.countWaysMemo( N, S, i, k-1)
            TrueR,FalseR = self.countWaysMemo( N, S, k+1, j)
            
            if S[k] == '|':
                tempT += TrueL*FalseR + TrueL*TrueR + FalseL*TrueR
                tempF += FalseL*FalseR
                
            elif S[k] == '&':
                tempT += TrueL*TrueR
                tempF += TrueL*FalseR +  FalseL*FalseR + FalseL*TrueR
                
            else:
                tempT += TrueL*FalseR + FalseL*TrueR
                tempF += TrueL*TrueR + FalseL*FalseR 
        
        self.memo[(i,j)] = [tempT, tempF]
        return [tempT, tempF]
                
   
        
    def countWays(self, N, S):
        # code here 
        return self.countWaysMemo(N,S, 0, len(S)-1)[0]%1003
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends