"""Reversing Elements Of Queue


Problem Description

Given an array of integers A and an integer B. We need to reverse the order of the first B elements of the array, leaving the other elements in the same relative order.

NOTE: You are required to first insert elements into an auxiliary queue then perform Reversal of first B elements.



Problem Constraints

1 <= B <= length of the array <= 500000
1 <= A[i] <= 100000


Input Format

The argument given is the integer array A and an integer B.


Output Format

Return an array of integer after reversing the first B elements of A using queue.


Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
 B = 3

Input 2:

 A = [5, 17, 100, 11]
 B = 2



Example Output

Output 1:

 [3, 2, 1, 4, 5]

Output 2:

 [17, 5, 100, 11]



Example Explanation

Explanation 1:

 Reverse first 3 elements so the array becomes [3, 2, 1, 4, 5]

Explanation 2:

 Reverse first 2 elements so the array becomes [17, 5, 100, 11]"""

 """
 Hint 1
 This can be easily done by inserting first B elements in the queue and replace that value in the array A such that first B elements of array is reversed.
 """
"""
Solution Approach
The idea is to use an auxiliary queue.

1) Create an empty queue.
2) Append first B elements in the queue
3) One by one dequeue the elements from the queue and update the array at ith position. (Initially i = B-1)
4) Repeat 3 until queue is empty. Also, decrement i by one at each step.
"""


from collections import deque
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        if n < 2:
            return A
        q = deque()
        for i in range(B):
            q.append(A[i])
        i = B - 1
        while len(q) != 0:
            A[i] = q.popleft()
            i -= 1
        return A

