"""
Palindromic patitioning


Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of given string.


Example 1:

Input: str = "ababbbabbababa"
Output: 3
Explaination: After 3 partitioning substrings 
are "a", "babbbab", "b", "ababa".

Example 2:

Input: str = "aaabba"
Output: 1
Explaination: The substrings after 1
partitioning are "aa" and "abba".


Your Task:
You do not need to read input or print anything, Your task is to complete the function palindromicPartition() which takes the string str as input parameter and returns minimum number of partitions required.


Expected Time Complexity: O(n*n) [n is the length of the string str]
Expected Auxiliary Space: O(n*n)


Constraints:
1 ≤ length of str ≤ 500"""

"""
Hint 1
For each index calculate total partitions required for palindrome partitioning of the string ending at i.
"""
#User function Template for python3

class Solution:
    
    def __init__(self):
        self.memo = {}
        
    def checkPalindrome(self, string, i, j):
        # temp = string[i:j+1]
        N= j-i+1
        
        for k in range(N//2):
            if  string[i+k] != string[j-k]:
                return False
                
        return True
        
    # def palindromicPartitionMemo(self, string, i , j):
        
    #     if i==j or self.checkPalindrome(string,i,j):
    #         return 0
        
    #     if (i,j) in self.memo:
    #         return self.memo[(i,j)]
        
    #     temp = j-i+1
        
    #     for k in range(i, j):
    #         lt = self.palindromicPartitionMemo( string, i , k )
    #         rt = self.palindromicPartitionMemo( string, k+1, j )
    #         temp = min(temp, lt+rt+1 )

    #     self.memo[(i,j)] = temp
        
    #     return temp

    # def palindromicPartitionTable(self, string):

    #     N = len(string)
    #     t = [[ 0 for i in range(N) ] for j in range(N) ] 
        
        
    #     for L in range(1, N+1):
    #         for i in range(0, N-L+1):
    #             j = i+L-1
                
    #             if tp[i][j] == True or self.checkPalindrome(string ,i , j):
    #                 t[i][j] = 0
    #                 continue
                
    #             temp = L
                
    #             for k in range(i, j):
    #                 lt = t[i][k]
    #                 rt = t[k+1][j]
                    
    #                 temp = min(temp, lt+rt+1 )

    #             t[i][j] = temp
    #     # print(t)
    #     return t[0][-1]
    
    def palindromicPartitionTable2(self, string):

        N = len(string)
        
        t = [ 0 for i in range(N) ] 
        tp = [[ False for i in range(N) ] for j in range(N) ] 
        
        for i in range(N):
            tp[i][i] = True

        for L in range(1, N+1):
            for i in range(N-L+1):
                j = i + L - 1
                
                if string[i] == string[j] and ( j-i<2 or tp[i+1][j-1] ):
                    tp[i][j] = True


        for i in range(N):
            if tp[0][i]:
                t[i] = 0
            else:
                t[i] = float('inf')
                for j in range(i):
                    if tp[j+1][i]:
                        t[i] = min(t[i], 1+t[j])
                        
        # print(t)
        return t[N-1]
    
        
    def palindromicPartition(self, string):
        # code here
        # return self.palindromicPartitionMemo( string, 0 , len(string)-1)\
        # return self.palindromicPartitionTable( string)
        return self.palindromicPartitionTable2( string)
        

            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends