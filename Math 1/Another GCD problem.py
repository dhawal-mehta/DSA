"""Another GCD problem


Problem Description

Given an integer array A of size N. Find the maximum length of a subarray Al, Al+1 ... Ar such that gcd(A[l], A[l+1], ... A[r]) > 1.

NOTE: If no such subarray exists, return -1.



Problem Constraints

1 <= N <= 105
0 <= A[i] <= 106


Input Format

First and only argument is an integer array A of size N.


Output Format

Return an integer denoting the maximum length of a subarray.


Example Input

Input 1:

 A = [7, 1, 2, 3, 4]

Input 2:

 A = [2, 4, 6, 8, 20]



Example Output

Output 1:

 1

Output 2:

 5



Example Explanation

Explanation 1:

 Gcd of every two consecutive element is 1. So, we can not take more than 1 element in any subarray. So, the answer is 1.

Explanation 2:

 Gcd of all elements in the array is greater than 1 which is 2. So, the maximum length of the subarray is 5.

"""
def solve( A):
    def gcd(a,b):
        if a>b:
            return gcd(b,a)
        if b%a == 0:
            return a
        return gcd(b%a,a)
    
    if max(A) == 1:
        return -1

    maxl = 1
    currl = 1
    currgcd = A[0] 
    for i in range(1, len(A)):
        tmpgcd = gcd(currgcd, A[i])

        if tmpgcd > 1:
            currl += 1
            maxl = max(maxl, currl)
            currgcd = tmpgcd
        else:
            currgcd= A[i]
            currl = 1
            currl = 1

    currl = 1
    currgcd = A[-1] 
    for i in range(len(A)-2, -1, -1):
        tmpgcd = gcd(currgcd, A[i])

        if tmpgcd > 1:
            currl += 1
            maxl = max(maxl, currl)
            currgcd = tmpgcd
        else:
            currgcd= A[i]
            currl = 1

    return maxl
            