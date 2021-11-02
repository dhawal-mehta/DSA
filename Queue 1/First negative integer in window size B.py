"""
First negative integer in window size B

Problem Description

Given an array of integers A of size N and an integer B.

Find the first negative integer for each and every window(contiguous subarray) of size B.

If a window does not contain a negative integer, then return 0 for that window.



Problem Constraints

1 <= N <= 200000

-109 <= A[i] <= 109



Input Format

The arguments given are integer array A and integer B.


Output Format

Return an integer array of size N+1-B representing answer of the ith window.


Example Input

 Input 1:
    A = [-1, 2, 3, -4, 5]
    B = 2


Input 2: A = [-8, 2, 3, -6, 10] B = 2



Example Output

Output 1:
    [-1, 0, -4, -4] 
Output 2:
    [-8, 0, -6, -6]



Example Explanation

Explaination For Input:-1 
    window [2,3] doesn't contain any negative integer so it's answer will be 0 and rest all the windows have some negative integer.
"""
"""
Hint 1
This problem is the variation of sliding window problem.

Try to think according to that perspective.
"""
# @param A : list of integers
# @param B : integer
# @return a list of integers
def solve(A, B):
    q = []
    
    start = 0
    ans = []
    end=0
    
    # for i in range( len(A) ):
        
    #     if A[i] < 0:
    #         q.append(i)
            
    #     while start+1 < len(q) and q[start] + B-1 < i:
    #             start += 1
        
    #     if i >= B-1:
    #         if len(q) > start:
    #             if  q[start]+ B - 1 < i:
    #                 ans.append(0)
    #             else:
    #                 ans.append(A[ q[start] ])
    #         else:
    #             ans.append(0)
            
    
    # # print(ans)
    # return ans
    
    
    Q = []
    start = 0
    
    ans = []
    
    for i in range( len(A) ):
        if A[i] < 0:
            Q.append(i)
            
    
    for i in range(len(A)-B+1):
        while len(Q)-start > 0 and Q[start]<i:
            start+=1
        
        if len(Q)-start > 0 and Q[start] >= i and Q[start] < i+B:
            ans.append(A[Q[start]])
        else:
            ans.append(0)
        

    return ans