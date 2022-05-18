"""Knapsack with Duplicate Items


Given a set of N items, each with a weight and a value, represented by the array w[] and val[] respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.

 

Example 1:

Input: N = 2, W = 3
val[] = {1, 1}
wt[] = {2, 1}
Output: 3
Explanation: 
1.Pick the 2nd element thrice.
2.Total profit = 1 + 1 + 1 = 3. Also the total 
  weight = 1 + 1 + 1  = 3 which is <= W.

 

Example 2:

Input: N = 4, W = 8
val[] = {1, 4, 5, 7}
wt[] = {1, 3, 4, 5}
Output: 11
Explanation: The optimal choice is to 
pick the 2nd and 4th element.

 

Your Task:
You do not need to read input or print anything. Your task is to complete the function knapSack() which takes the values N, W and the arrays val[] and wt[] as input parameters and returns the maximum possible value.

 

Expected Time Complexity: O(N*W)
Expected Auxiliary Space: O(W)

 

Constraints:
1 ≤ N, W ≤ 1000
1 ≤ val[i], wt[i] ≤ 100
"""
#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        #-----------------------memoization ( gave stack overflow )-------------------
        
        # memo = {}
        # def util(N, wt, val, cap, curr):
            

            
        #     if curr >= N or cap==0:
        #         return 0
            
        #     if (cap, curr) in memo:
        #         return memo[(cap, curr)]
            
        #     # print(wt[curr], cap)
        #     if wt[curr] <= cap:
        #   
        #         temp = max( val[curr] + util(N, wt, val, cap-wt[curr], curr),
        #                 util(N,wt,val,cap,curr+1)
        #             )
        #     else:
        #        
        #         temp = util(N,wt,val,cap, curr+1)
            
        #    
        #     memo[(cap ,curr)] = temp
        #     return temp
                
        # return util(N, wt, val, W, 0)
            
        #-------------------------tablular ( type 1)----------------------
        # t = [0 for i in range(W+1)]
        
        # for i in range(1, W+1):
        #     temp = 0
            
        #     for j in range(N):
                
        #         if wt[j] <= i:
        #             temp = max(temp, val[j] + t[i-wt[j]] )
            
        #     t[i] = temp
        
        # # print(t)
        # return t[-1]


        #---------------------------tablular ( type 2)--------------------------
        t = [ [0 for j in range(W+1)] for i in range(N+1) ]
        
        for i in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    t[i][j] =  max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j] )
                else:
                    t[i][j] = t[i-1][j]
        
        # print(t)
        return t[-1][-1]
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends