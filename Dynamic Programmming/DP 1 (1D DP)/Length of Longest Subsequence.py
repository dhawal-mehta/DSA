"""Length of Longest Subsequence


Given an array of integers, A of length N, find the length of longest subsequence which is first increasing then decreasing.

Input Format:

The first and the only argument contains an integer array, A.

Output Format:

Return an integer representing the answer as described in the problem statement.

Constraints:

1 <= N <= 3000
1 <= A[i] <= 1e7

Example:

Input 1:
    A = [1, 2, 1]

Output 1:
    3

Explanation 1:
    [1, 2, 1] is the longest subsequence.

Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]

Output 2:
    6

Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.
"""
"""
Hint 1

Try to come up with something which stores length of increasing sequence upto a particular index and length of decreasing sequence from that particular index.

Can you think of DP for either of the task.

"""
"""
Solution Approach

The problem can be solved as follows:

    Construct array inc[i] where inc[i] stores Longest Increasing subsequence ending with A[i]. This can be done simply with O(n^2) DP.

      inc[i]=1
      for j from 0 to i-1
          if A[j]<A[i]
              inc[i]=max(inc[i],inc[j]+1)

    Construct array dec[i] where dec[i] stores Longest Decreasing subsequence ending with A[i]. This can be done simply with O(n^2) DP.

      dec[i]=1
      for j from i+1 to n-1
          if A[j]>A[i]
              dec[i]=max(dec[i],dec[j]+1)

    Now we need to find the maximum value of (inc[i] + dec[i] - 1)
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lslUtil(self,A):
        lis = [1]*len(A)
        lds = [1]*len(A)
        
        for i in range(1,len(A)):
            for j in range(0,i):
                if A[i] > A[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                   # break;
                    
        for i in range(len(A) - 2,-1,-1):
            for j in range(len(A)-1,i,-1):
                if A[i] > A[j] and lds[i] < lds[j] + 1:
                    lds[i] = lds[j] + 1
                    # break;
       
                    
       # print(lis)
       ## print(lds)
        max_ = lis[0] + lds[0]
        for i in range(1,len(A)):
            if lis[i] + lds[i] > max_:
                max_ = lis[i] + lds[i]
                
        return max_ - 1
        
    def longestSubsequenceLength(self, A):
        if len(A) == 0 or len(A) == 1:
            return len(A)
        return self.lslUtil(A)
