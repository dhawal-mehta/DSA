"""
Minimum sum partition


Given an integer array arr of size N, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference


Example 1:

Input: N = 4, arr[] = {1, 6, 11, 5} 
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11   

Example 2:

Input: N = 2, arr[] = {1, 4}
Output: 3
Explanation: 
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {4}, sum of Subset2 = 4


Your Task:  
You don't need to read input or print anything. Complete the function minDifference() which takes N and array arr as input parameters and returns the integer value


Expected Time Complexity: O(N*|sum of array elements|)
Expected Auxiliary Space: O(N*|sum of array elements|)


Constraints:
1 ≤ N*|sum of array elements| ≤ 106"""
"""
Hint 1
Generate a 2D array for DP where, dp[index][sum] = min posssible difference, if index is the index of next element, and sum is the sum of all elements selected.
"""

#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		memo = {}
		def util(arr,n, w, start):
            
            if w < 1:
                return 0 
            
            if start >= n:
                return 0
            
            if (w,start) in memo:
                return memo[ (w,start) ]
            
            if arr[start] <= w:
                temp =  max(
                    arr[start] + util(arr, n, w-arr[start], start+1) , 
                    util(arr, n, w, start+1)
                )
            else:
                temp =  util(arr, n, w, start+1)
            
            memo[(w,start)] = temp
            return temp
            
        temp = util(arr, n, sum(arr)/2, 0)
        
        # print(temp)
        
        return sum(arr) - 2*temp
                
        
		 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends