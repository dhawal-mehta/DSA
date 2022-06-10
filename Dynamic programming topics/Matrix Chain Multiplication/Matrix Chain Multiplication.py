"""
Matrix Chain Multiplication


Given a sequence of matrices, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1) where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Example 1:

Input: N = 5
arr = {40, 20, 30, 10, 30}
Output: 26000
Explaination: There are 4 matrices of dimension 
40x20, 20x30, 30x10, 10x30. Say the matrices are 
named as A, B, C, D. Out of all possible combinations,
the most efficient way is (A*(B*C))*D. 
The number of operations are -
20*30*10 + 40*20*10 + 40*10*30 = 26000.


Example 2:

Input: N = 4
arr = {10, 30, 5, 60}
Output: 4500
Explaination: The matrices have dimensions 
10*30, 30*5, 5*60. Say the matrices are A, B 
and C. Out of all possible combinations,the
most efficient way is (A*B)*C. The 
number of multiplications are -
10*30*5 + 10*5*60 = 4500.


Your Task:
You do not need to take input or print anything. Your task is to complete the function matrixMultiplication() which takes the value N and the array arr[] as input parameters and returns the minimum number of multiplication operations needed to be performed.


Expected Time Complexity: O(N3)
Expected Auxiliary Space: O(N2)


Constraints: 
2 ≤ N ≤ 100
1 ≤ arr[i] ≤ 500
"""
"""
Hint 1
For each pattern of parenthesis try to find out the number of multiplications required.
"""
"""
Hint 2

Use the optimal substructure property to solve it within the time limit.
"""
#User function Template for python3

class Solution:
    # def __init__(self):
        # self.memo = {}
        # self.memo = [ [-1 for i in range(102)]  for j in range(102) ]


    # def matrixMultiplicationMemo(self,arr, start, end):
    #     if start >= end:
    #         return 0
        
    #     if (start, end) in self.memo:
    #         return self.memo[(start,end)]
            
    #     temp =  10**9
    #     for k in range(start, end):
    #         l = self.matrixMultiplicationMemo(arr, start, k)
    #         r = self.matrixMultiplicationMemo(arr, k+1, end)
            
    #         temp = min(temp, l + r + arr[start-1]*arr[k]*arr[end])
        
    #     self.memo[(start,end)] = temp
        
    #     return temp

    # def matrixMultiplicationMemo2(self,arr, start, end):
    #     if start >= end:
    #         return 0
        
    #     if self.memo[start][end] != -1:
    #         return self.memo[start][end]
            
    #     temp =  10**9
    #     for k in range(start, end):
    #         l = self.matrixMultiplicationMemo2(arr, start, k)
    #         r = self.matrixMultiplicationMemo2(arr, k+1, end)
            
    #         temp = min(temp, l + r + arr[start-1]*arr[k]*arr[end])
        
    #     self.memo[start][end] = temp
        
    #     return temp
    
        
    def matrixMultiplicationTable(self,arr, N):
        
        memo = [ [0 for i in range(N)]  for j in range(N) ]
            
        # for i in range(102):
        #     memo[0][i] = 0
            
        # it starts from 2 as min we need 2 matrix to multiply
        # N+1 has no effect here as it inner loop fails for L=N , L in range(2,N) will also do
        # i=>start, j=>end, L=>current length of Matrix chain
        for L in range(2, N+1):
            for i in range(1, N-L+1):
                
                j = i+L-1
                temp =  10**9
                for k in range(i, j):

                    l = memo[i][k]
                    r = memo[k+1][j]
                    temp = min(temp, l + r + arr[i-1]*arr[k]*arr[j])
                
                memo[i][j] = temp
                
        # print(memo)
        return memo[1][-1]
            
        
    def matrixMultiplication(self, N, arr):
        # code here
        # return self.matrixMultiplicationMemo(arr, 1, N-1)
        # return self.matrixMultiplicationMemo2(arr, 1, N-1)  
        return self.matrixMultiplicationTable(arr, N)  

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
