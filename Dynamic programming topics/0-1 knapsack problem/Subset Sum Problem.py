"""
Subset Sum Problem


Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1 
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.

Example 2:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 30
Output: 0 
Explanation: There is no subset with sum 30.


Your Task:  
You don't need to read input or print anything. Your task is to complete the function isSubsetSum() which takes the array arr[], its size N and an integer sum as input parameters and returns boolean value true if there exists a subset with given sum and false otherwise.
The driver code itself prints 1, if returned value is true and prints 0 if returned value is false.
 

Expected Time Complexity: O(sum*N)
Expected Auxiliary Space: O(sum*N)
 

Constraints:
1 <= N <= 100
1<= arr[i] <= 100
1<= sum <= 105
"""

class Solution:
    def isSubsetSum (self, N, arr, s):
        # code here 
        
        # Using memoization (top-down approach)
        # memo = {}
        
        # def util(arr, N, s, start):
            
        #     if s == 0:
        #         return True
            
        #     if start >= N:
        #         return False
            
        #     if (s,start) in memo:
        #         return memo[(s,start)]
                
        #     if  arr[start] <= s:
        #         temp = (util(arr, N, s-arr[start], start+1) or util(arr, N, s, start+1))
            
        #     else:
        #         temp = util(arr, N, s, start+1)
            
        #     memo[(s, start)] = temp
        #     return temp
            
        # return 1 if util(arr, N , s, 0) else 0
        


        # using tabulation method( bottom up approach)
        t = [ [ -1 for j in range(s+1) ] for i in range(N+1)]
        
        
        for i in range( N + 1 ):
            for j in range( s + 1 ):
                
                if i==0 or j == 0:
                    t[i][j] = True if j==0 else False
                    continue
                
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
                else:
                    t[i][j] = t[i-1][j] 
        
        # for i in range(N+1):
        #     print(t[i])
            
        return 1 if t[-1][-1] else 0 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends