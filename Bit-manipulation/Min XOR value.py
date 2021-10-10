"""Min XOR value
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA

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



Example Explanation

Explanation 1:

 0 xor 2 = 2
"""
"""
Hint 2
The brute-force would be to try every pair (x, y).

If the array is sorted, do you need to check for every pair? Try to reduce the number of checked pairs.
"""
"""
Hint 1
Hint: Sort the array.

Think of how you can use the sorted array to find the minimum XOR.
"""
"""
The first step is to sort the array. The answer will be the minimal value of X[i] XOR X[i+1] for every i.

Proof:
Let’s suppose that the answer is not X[i] XOR X[i+1], but A XOR B and there exists C in the array such as A <= C <= B.

Next is the proof that either A XOR C or C XOR B are smaller than A XOR B.

Let A[i] = 0/1 be the i-th bit in the binary representation of A
Let B[i] = 0/1 be the i-th bit in the binary representation of B
Let C[i] = 0/1 be the i-th bit in the binary representation of C

This is with the assumption that all of A, B and C are padded with 0 on the left until they all have the same length

Example: A=169, B=187, C=185

A=101010012
B=101110112
C=101110012

Let i be the leftmost (biggest) index such that A[i] differs from B[i]. There are 2 cases now:
1) C[i] = A[i] = 0,
then (A XOR C)[i] = 0 and (A XOR B)[i] = 1
This implies (A XOR C) < (A XOR B)
2) C[i] = B[i] = 1,
then (B XOR C)[i] = 0 and (A XOR B)[i] = 1
This implies (B XOR C) < (A XOR B)

Time complexity: O(N * logN) to sort the array and O(N) to find the smallest XOR
Space complexity: O(N)
"""
# @param A : list of integers
# @return an integer
def findMinXor(A):
    A = sorted(A)
    minXor = (2**32)  - 1
    for i in range(len(A)-1):
        xor = A[i]^A[i+1]
        
        if xor < minXor:
            minXor = xor
    
    return minXor
