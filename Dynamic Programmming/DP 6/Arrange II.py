"""Arrange II


You are given a sequence of black and white horses, and a set of K stables numbered 1 to K. You have to accommodate the horses into the stables in such a way that the following conditions are satisfied:

        You fill the horses into the stables preserving the relative order of horses. For instance, you cannot put horse 1 into stable 2 and horse 2 into stable 1. You have to preserve the ordering of the horses.
        No stable should be empty and no horse should be left unaccommodated.
        Take the product (number of white horses * number of black horses) for each stable and take the sum of all these products. This value should be the minimum among all possible accommodation arrangements

Example:

Input: {WWWB} , K = 2
Output: 0

Explanation:
We have 3 choices {W, WWB}, {WW, WB}, {WWW, B}
for first choice we will get 1*0 + 2*1 = 2.
for second choice we will get 2*0 + 1*1 = 1.
for third choice we will get 3*0 + 0*1 = 0.

Of the 3 choices, the third choice is the best option. 

If a solution is not possible, then return -1"""

"""
Hint 1

Hint : Dynamic programming

Can we use the fact that the order should be preserved ? Could you create a recurrence relation using it ?
You can have a state around [first X number of horses, first Y number of stables].

"""
"""
Solution Approach

Recurrence relation


Rec(Current_Horse, Current_Stable) =  |   
                                      |           |
                                      |           |Rec(i + 1, Next_Stable) + (White_Horses * Black Horses in Current_Stable)  
                                      |       min |
                                      |           |
                                      |   
                                      | i = Current_Horse to Number_of_Horses  
                                      |      



Now can you implement it?

Happy Coding

"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):
        dp = [ [ 0 for i in  range(len(A)) ] for j in range(B+1) ]
        
        if B == len(A):
            return 0
        elif B > len(A):
            return -1

        white = 0 
        black = 0 
        
        for i in range(0, len(A)):
            if A[i] == 'W':
                white += 1
            else:
                black += 1
                
            dp[1][i] = white*black
        
        # print(dp)
        
        for stable  in range(2, B+1):
            for end in range(stable-1, len(A)):
                white = 0 
                black = 0 
                temp = float('inf')
                
                for k in range(end, 0, -1):
                    if A[k] == 'W':
                        white+=1
                    else:
                        black+=1
                        
                    temp = min(temp, dp[stable-1][k-1] + white*black)
                    
                dp[stable][end]  = 0 if temp == float('inf') else temp
                
                # print(dp)
        
        return dp[B][len(A)-1]
        