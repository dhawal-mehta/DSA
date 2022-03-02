"""Number of Coins

Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


Example 1:

Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin

Example 2:

Input: V = 11, M = 4,coins[] = {9, 6, 5, 1} 
Output: 2 
Explanation: Use one 6 cent coin
and one 5 cent coin


Your Task:  
You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as input parameters and returns the answer.

Expected Time Complexity: O(V*M)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V*M ≤ 106
All array elements are distinct"""

"""
Hint 1

 Let us define the state dp(i) as the answer to the question: what is the minimum number of coins we need to get value i. Then:

    If i == 0, then there is need no coins at all, so we return 0.
    if i < 0, so we are trying to make a negative-sum, which is not possible, so we return minus infinity as an indicator that it is not possible.
    In other case, we check all dp(i - coin) for every coin and add 1 to the result.

Complexity:  O(V * M), where M is the number of coins, because: we have O(V) different states and we have M choices to go from any state.
"""
"""
Hint 2

The recursive formula is a follows:
If V == 0, then 0 coins required.
If V > 0:
minCoins(coins[0..m-1], V) = 
min {1 + minCoins(V-coin[i])},
    where i varies from 0 to m-1
    and coin[i] <= V 
"""
#User function Template for python3
class Solution:
    
    # def __init__(self):
    #     import sys
        
	def minCoins(self, coins, M, V):
		# code here

		# t = [ [0 for j  in range(V+1)] for i in range(M+1) ]
		
		# INT_MAX = 10**9
		
		# for i in range(1, V+1):
		#     t[0][i] = INT_MAX
		
        # for i in range(1, M+1):
        #     for j  in range(1, V+1):
                
        #         if coins[i-1] <= j:
        #             t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
                    
        #         else:
        #             t[i][j] = t[i-1][j]
                    
        # return t[-1][-1] if t[-1][-1] != INT_MAX else -1
        
        INT_MAX = 10**9
		t = [ INT_MAX for i in range(V+1) ]
		t[0] = 0
		
        for i in range(1, V+1):
            for j  in range(M):
                if coins[j] <= i:
                    t[i] = min(1+t[ i-coins[j] ], t[i] )
                    
        return t[-1] if t[-1] != INT_MAX else -1
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends