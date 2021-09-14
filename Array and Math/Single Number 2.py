"""
Single Number II

Problem Description

Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?



Problem Constraints

    2 <= A <= 5*106

    0 <= A <= INTMAX



Input Format

First and only argument of input contains an integer array A.


Output Format

Return a single integer.


Example Input

Input 1:

 A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

Input 2:

 A = [0, 0, 0, 1]



Example Output

Output 1:

 4

Output 2:

 1



Example Explanation

Explanation 1:

 4 occurs exactly once in Input 1.
 1 occurs exactly once in Input 2.
"""

"""
Hint1 

Let us look at every bit position.

Every number that occurs thrice will either contribute 3 ‘1’s or 3 ‘0’s to the position.

The number that occurs once X will contribute exactly one 0 or 1 to the position depending on whether it has 0 or 1 in that position.

So:

    If X has 1 in that position, we will have (3x+1) number of 1s in that position.
    If X has 0 in that position, we will have (3x+1) number of 0s in that position.

Can you think of a solution using the above observation?


"""

"""
Solution Approach 

Having noticed that if X has 1 in that position, we will have 3x+1 number of 1s in that position. If X has 0 in that position, we will have 3x+1 number of 0 in that position.

A straightforward implementation is to use an array of size 32 to keep track of the total count of ith bit.

We can improve this based on the previous solution using three bitmask variables:

ones as a bitmask to represent the ith bit had appeared once.
twos as a bitmask to represent the ith bit had appeared twice.
threes as a bitmask to represent the ith bit had appeared three times.
When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0. The final answer will be the value of ones.

"""

""" accepted solution """

# @param A : tuple of integers
# @return an integer
def singleNumber(self, A):
    INT_SIZE = 32
    res = 0
    for i in range(0,INT_SIZE):
        sm = 0
        bit = 1 << i
        for j in A:
            if j & bit:
                sm += 1
                
        if sm%3:
            res = res | bit
    
    return res