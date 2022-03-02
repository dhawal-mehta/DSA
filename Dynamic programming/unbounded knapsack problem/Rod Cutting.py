"""
Rod Cutting


Given a rod of length N inches and an array of prices, price[] that contains prices of all pieces of size smaller than N. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

 

Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.

Example 2:

Input:
N=8
Price[] = {3, 5, 8, 9, 10, 17, 17, 20}
Output: 24
Explanation: 
The maximum obtainable value is 
24 by cutting the rod into 8 pieces 
of length 1, i.e, 8*3=24. 


Your Task:  
You don't need to read input or print anything. Your task is to complete the function cutRod() which takes the array A[] and its size N as inputs and returns the maximum price obtainable.


Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 1000
1 ≤ Ai ≤ 105
"""
"""
Hint 1
This is a dp problem where you need to store the states so as to avoid overlapping cases.The dp state for this problem is maximum price for length 'x'.
"""
#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here

        # -------------------------------Via 1-d array--------------------------
        # t = [ 0 for i in range(n+1)]
       
        # for i in range(1,n+1):
            
        #     temp = price[i-1]
            
        #     for j in range(i):
        #         temp = max(temp, t[j] + t[i-j] )
            
        #     t[i] = temp
        
        # return t[-1]
        
        # -------------------------------Via 2-d array--------------------------
        t = [ [0  for j in range(n+1)] for i in range(n+1) ]
        length = [ i+1 for i in range(n) ]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if length[i-1] <= j:
                    t[i][j] = max(t[i-1][j], price[i-1] + t[i][j - length[i-1]] )
                else:
                    t[i][j] = t[i-1][j]
                    
        return t[-1][-1]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends