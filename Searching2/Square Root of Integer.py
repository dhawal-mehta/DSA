"""Square Root of Integer


Problem Description

Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.



Problem Constraints

0 <= A <= 1010


Input Format

The first and only argument given is the integer A.


Output Format

Return floor(sqrt(A))


Example Input

Input 1:

 11

Input 2:

 9



Example Output

Output 1:

 3

Output 2:

 3



Example Explanation

Explanation:

 When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
 When A = 9 which is a perfect square of 3, so we return 3."""

 """
 Hint 1

Think about the answer of this “Is a particular number r less than floor(sqrt(x))?”

Answer of the above problem as a function of r will look like [1,1,……1,0,0……0]. Can you use this fact to devise a solution now?
"""
"""
Solution Approach

Think in terms of binary search.

Let us say S is the answer.

We know that 0 <= S <= x.

Consider any random number r.

    If r*r <= x, S >= r

    If r*r > x, S < r.

Maybe try to run a binary search for S.
"""
# @param A : integer
# @return an integer
def sqrt(self, A):
    if A == 1:
        return 1
    ret = int(A ** 0.5)
    return ret
    low = 0
    high = A / 2 + 1
    while low + 1 < high:
        mid = low + (high - low) / 2
        square = mid ** 2
        if square == A:
            return mid
        elif square < A:
            low = mid
        else:
            high = mid
    return low
