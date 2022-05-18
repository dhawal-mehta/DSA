"""
Egg Dropping Puzzle


You are given N identical eggs and you have access to a K-floored building from 1 to K.

There exists a floor f where 0 <= f <= K such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break. There are few rules given below. 

    An egg that survives a fall can be used again.
    A broken egg must be discarded.
    The effect of a fall is the same for all eggs.
    If the egg doesn't break at a certain floor, it will not break at any floor below.
    If the eggs breaks at a certain floor, it will break at any floor above.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

For more description on this problem see wiki page

Example 1:

Input:
N = 1, K = 2
Output: 2
Explanation: 
1. Drop the egg from floor 1. If it 
   breaks, we know that f = 0.
2. Otherwise, drop the egg from floor 2.
   If it breaks, we know that f = 1.
3. If it does not break, then we know f = 2.
4. Hence, we need at minimum 2 moves to
   determine with certainty what the value of f is.

Example 2:

Input:
N = 2, K = 10
Output: 4

Your Task:
Complete the function eggDrop() which takes two positive integer N and K as input parameters and returns the minimum number of attempts you need in order to find the critical floor.

Expected Time Complexity : O(N*(K^2))
Expected Auxiliary Space: O(N*K)

Constraints:
1<=N<=200
1<=K<=200
"""
"""
Hint 1
The approach will be to make a table which will store the results of sub-problems so that to solve a sub-problem, it would only require a look-up from the table which will take constant time, which earlier took exponential time.
Formally for filling DP[i][j] state where ‘i’ is the number of eggs and ‘j’ is the number of floors: 
 

    We have to traverse for each floor ‘x’ from ‘1’ to ‘j’ and find minimum of: 
             (1 + max( DP[i-1][j-1], DP[i][j-x] )).
"""
"""
Hint 2
This simulation will make things clear: 
 

    i => Number of eggs 
    j => Number of floors 
    Look up find maximum 
    Lets fill the table for the following case: 
    Floors = ‘4’ 
    Eggs = ‘2’
    1 2 3 4
    1 2 3 4 => 1 
    1 2 2 3 => 2 
    For ‘egg-1’ each case is the base case so the 
    number of attempts is equal to floor number.
    For ‘egg-2’ it will take ‘1’ attempt for 1st 
    floor which is base case.
    For floor-2 => 
    Taking 1st floor 1 + max(0, DP[1][1]) 
    Taking 2nd floor 1 + max(DP[1][1], 0) 
    DP[2][2] = min(1 + max(0, DP[1][1]), 1 + max(DP[1][1], 0))
    For floor-3 => 
    Taking 1st floor 1 + max(0, DP[2][2]) 
    Taking 2nd floor 1 + max(DP[1][1], DP[2][1]) 
    Taking 3rd floor 1 + max(0, DP[2][2]) 
    DP[2][3]= min(‘all three floors’) = 2
    For floor-4 => 
    Taking 1st floor 1 + max(0, DP[2][3]) 
    Taking 2nd floor 1 + max(DP[1][1], DP[2][2]) 
    Taking 3rd floor 1 + max(DP[1][2], DP[2][1]) 
    Taking 4th floor 1 + max(0, DP[2][3]) 
    DP[2][4]= min(‘all four floors’) = 3 

"""
#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def __init__(self):
        self.memo = {}
        
    # def eggDropMemo(self,n, k):
    #     # code here
    #     if k<=1:
    #         return k
            
    #     if n<=1:
    #         return k
        
    #     if (n,k) in self.memo:
    #         return self.memo[(n,k)]
            
    #     ans = float('inf')
        
    #     for i in range(1, k+1):
    #         temp = max( self.eggDropMemo(n-1, i-1), self.eggDropMemo(n, k-i) )
    #         ans = min(ans, temp)
        
    #     self.memo[(n,k)] = ans + 1
    #     return ans+1
        
    def eggDrop(self,e, f):
            
        t = [ [ 0 for j in range(f+1) ] for i in range(e+1) ]
        
        for j in range( f+1):
            t[1][j] = j
        
        for i in range(1, e+1):
            t[i][1] = 1
    
        
        for i in range(2, e+1 ):
            
            for j in range(2, f+1):
                ans = j
                
                for k in range(2, j+1):
                    temp = 1+max( t[i-1][k-1], t[i][j-k] )
                    
                    ans = min(temp, ans)
                
                t[i][j] = ans
                
        return t[e][f]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends
