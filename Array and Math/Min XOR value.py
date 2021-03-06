"""
Min XOR value

Problem Description

Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.


Problem Constraints

2 <= length of the array <= 100000
0 <= A[i] <= 109


Input Format

First and only argument of input contains an integer array A.


Output Format

Return a single integer denoting minimum xor value.


Example Input

Input 1:

 A = [0, 2, 5, 7]

Input 2:

 A = [0, 4, 7, 9]



Example Output

Output 1:

 2

Output 2:

 3
 
"""
"""
hint 1

Hint: Sort the array.

Think of how you can use the sorted array to find the minimum XOR.

"""


""" accepted solution """
# @param A : list of integers
# @return an integer
def findMinXor( A):
    A = sorted(A)
    minXor = (2**32)  - 1
    for i in range(len(A)-1):
        xor = A[i]^A[i+1]
        
        if xor < minXor:
            minXor = xor
    
    return minXor