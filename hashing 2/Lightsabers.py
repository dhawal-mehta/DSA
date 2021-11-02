""" Lightsabers

Given two array of integers A and B of size N and M respectively.

The goal is to select some continuous interval in A such that there are exactly
B[0] elements with value 1, B[1] elements with value 2 and so on
ending with B[m-1] elements with value m.

However, it is not always possible to select such an interval form the given array therefore it is allowed
to remove some elements from A in order to achieve the goal.

Find and return the minimum number of elements to be removed from A in order to achieve the goal.
If it is not possible to achieve the goal return -1 instead.



Input Format

The first argument given is the integer array A.
The second argument given is the integer array B.

Output Format

Return the minimum number of elements to be removed from A in order to achieve the goal and 
if it is not possible to achieve the goal return -1 instead.

Constraints

1 <= N, M <= 100000
1 <= A[i] <= M
0 <= B[i] <= N

For Example

Input 1:
    A = [1, 2, 3, 4, 1]
    B = [2, 1, 1, 0]
Output 1:
    1   (Reomve element 4 and consider all the remaining elements).

Input 2:
    A = [1, 1, 2, 2, 2]
    B = [1, 2, 1]
Output 2:
    -1

"""
"""
Hint 1
Try it with hashing and 2 pointer technique.
"""
# @param A : list of integers
# @param B : list of integers
# @return an integer
def solve(A, B):
    
    goal = {}
    work = {}
    lastCount = 0
    
    for i in range(len(B)):
        if B[i] > 0:
            goal[i+1] = B[i]
            work[i+1] = 0
            lastCount += B[i]
            
    minCount = 0
    
    start = 0
    
    minStart = -1
    minEnd = len(A)
    
    for end in range(len(A)):
        
        if A[end] in goal:
            work[ A[end] ] += 1
            
            if work[ A[end] ] <= goal[ A[end] ]:
                minCount += 1
        
            if minCount == lastCount:

                while start < len(A) and ( A[start] not in goal or work[A[start]] > goal[A[start]] ):
                    if A[start] in goal:
                        work[A[start]] -= 1
                    
                    start += 1
            
                if end-start < minEnd-minStart:
                    minStart = start
                    minEnd = end
            
    
    # extraCount = 0
    
    if minStart == -1:
        return -1

    
    return minEnd-minStart+1 - lastCount