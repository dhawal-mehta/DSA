"""
Counting Triangles


You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

    You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

    Return answer modulo 109 + 7.

For example,

A = [1, 1, 1, 2, 2]

Return: 4

"""
"""
Hint 1
We know that for side lengths A, B and C where A < B < C, they form a triangle if they follow the triangle inequality i.e.

    A + B > C

Suppose you are given a sorted array of side lengths in ascending order. How will you count the possible number of triangles ?
"""
"""
Solution Approach

First we sort the array of side lengths. So since Ai < Aj < Ak where i < j < k, therefore it is sufficient to check Ai + Aj > Ak to prove they form a triangle.

Thus for every i and j, we can find the maximum value of k such that the triangle inequality holds.
Also we can also prove that for every such index i, we only have to increase the value of the k (satisfying the above condition) for every iteration of j from i+1 to n. Therefore, we get a O(n2) solution (Proof of this is left to the reader).
"""

def nTriang(A):
    
    A = sorted(A)
    ans = 0
    for i in range(len(A)-1,0,-1):
        l = 0
        r = i-1
        while(l<r):
            if A[l] + A[r] > A[i]:
                ans += r - l
                r -= 1
            else:
                l += 1     
    
    return ans
