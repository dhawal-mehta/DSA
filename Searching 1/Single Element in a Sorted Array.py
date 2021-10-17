"""Single Element in a Sorted Array

Problem Description

Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

NOTE: Users are expected to solve this in O(log(N)) time.


Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 10^9



Input Format

The only argument given is the integer array A.


Output Format

Return the single element that appears only once.


Example Input

Input 1:

A = [1, 1, 7]

Input 2:

A = [2, 3, 3]



Example Output

Output 1:

 7

Output 2:

 2



Example Explanation

Explanation 1:

 7 appears once

Explanation 2:

 2 appears once
"""
"""
Hint 1

You need to return the index of 1-time occuring element >= x.
You can do this by binary search.
"""
"""
Solution Approach

You need to return the index of 1 time occuring element >= x.
You can do this by binary search.
Note that this is classic binary search. Instead of looking for the element x,
you are looking for the least elements >= x.
You can do this by binary search.
Look for its implementation. There are multiple ways to do this.
Remember that index starts from 0
"""
# @param A : list of integers
# @return an integer
def util( A,l, r):
    m = l + (r - l)//2
    if m==0 and A[m] != A[m-1]:
        return A[m]
    elif m==len(A)-1 and A[m]!=A[m-1]:
        return A[m]
    elif A[m]!=A[m-1] and A[m]!= A[m+1]:
        return A[m]
    
    if m%2 == 0:
        if A[m]==A[m+1]:
            return util(A, m+1, r)
        else:
            return util(A,l,m-1)
    else:
        if A[m]==A[m-1]:
            return util(A, m+1, r)
        else:
            return util(A,l,m-1)
        
    
def solve( A):
    return util(A,0,len(A)-1)