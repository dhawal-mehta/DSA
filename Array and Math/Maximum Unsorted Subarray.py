"""
Maximum Unsorted Subarray

Problem Description

Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted. If A is already sorted, output -1.


Problem Constraints

1 <= N <= 1000000
1 <= A[i] <= 1000000


Input Format

First and only argument is an array of non-negative integers of size N.


Output Format

Return an array of length 2 where First element denotes the starting index(0-based) and second element denotes the ending index(0-based) of the sub-array. If the array is already sorted, return an array containing only one element i.e. -1.


Example Input

Input 1:

A = [1, 3, 2, 4, 5]

Input 2:

A = [1, 2, 3, 4, 5]



Example Output

Output 1:

[1, 2]

Output 2:

[-1]



Example Explanation

Explanation 1:

If we sort the sub-array A1, A2, then the whole array A gets sorted.

Explanation 2:

A is already sorted.
"""

"""
Hint 1
Assume that Al, …, Ar is the minimum-unsorted-subarray which is to be sorted, then subarrays A0, …, Al-1 and Ar+1, …, AN-1 will be in sorted(ascending) order.

How would you solve now?

"""
"""
Solution Approach

Assume that Al, …, Ar is the minimum-unsorted-subarray which is to be sorted.
then min(Al, …, Ar) >= max(A0, …, Al-1)
and max(Al, …, Ar) <= min(Ar+1, …, AN-1)
You can use this to observe and solve.
How would you solve now?
You can use 2 pointer technique to solve this question.

"""

"""
Accepted solution ( bad Approach )

def subUnsort(self, A):
    A_dash = sorted(A)
    
    start = -1
    end = -1
    
    flag =0
    for i in range(len(A)):
        if A[i] != A_dash[i]:
            if start==-1:
                flag=1
                start =i
                end = i
            else:
                end = i
    if flag==0:
        return [-1]
        
    return [start, end]
                
"""

""" Accepted solution (good approach) """
def subUnsort( A):
    l = 0
    
    while l < len(A)-1 and A[l] <= A[l+1]:
        l+=1
        
    if l == len(A)-1:
        return [-1]
    
    r = len(A)-1
    while r > 0 and A[r] >= A[r-1]:
        r -= 1
        
    mx = A[l]
    mn = A[r]
    for i in range(l,r):
        mx = max(mx, A[i])
        mn = min(mn, A[i])
    
    l = -1
    while A[l+1]<=mn:
        l+=1
    
    r= len(A)
    while A[r-1] >= mx:
        r-=1
    
    return [l+1,r-1]


A = [1,3,2,4,5]

print( subUnsort(A) )