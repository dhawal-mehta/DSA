"""
Maximum height of staircase

Problem Description

Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks.

The first stair would require only one block, the second stair would require two blocks and so on.

Find and return the maximum height of the staircase.



Problem Constraints
0 <= A <= 109


Input Format

The only argument given is integer A.


Output Format

Return the maximum height of the staircase using these blocks.


Example Input

Input 1:

 A = 10

Input 2:

 20



Example Output

Output 1:

 4

Output 2:

 5
"""
"""
Hint 1

How many square blocks needed to create a staircase of height n ?
"""
"""
Solution Approach

Sum of natural numbers upto n is given by (n(n+1))/2

So you just have to find largest n such that (n(n+1))/2 is less or equal to A.
Why?
As,you have to find the maximum height so suppose maximum height is n then there must be stairs with height n,n-1,n-2…..1 also we have a total of A stairs so summation of the height of stairs must be less than or equal to A.

So doing binary search for n is the best approach for the problem.
"""
# @param A : integer
# @return an integer
def solve(self, A):
    def isPossible(n, A):
        return (True if (n*(n+1))//2 <= A else False)

    if A == 0:
        return 0
    
    l = 1
    r = A
    while l <= r:
        mid = l + (r-l)//2

        t1 = isPossible(mid, A)
        if t1 and not isPossible(mid+1, A):
            return mid
        
        if t1:
            l = mid+1
        else:
            r = mid-1
