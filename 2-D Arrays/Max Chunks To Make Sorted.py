"""Max Chunks To Make Sorted

Problem Description

Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)], if we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?



Problem Constraints

1 <= N <= 100000
0 <= A[i] < N


Input Format

The only argument given is the integer array A.


Output Format

Return the maximum number of chunks that we could have made.


Example Input

Input 1:

 A = [1, 2, 3, 4, 0]

Input 2:

 A = [2, 0, 1, 3]



Example Output

Output 1:

 1

Output 2:

 2



Example Explanation

Explanation 1:

 A = [1, 2, 3, 4, 0]
 To get the 0 in the first index, we have to take all elements in a single chunk.

Explanation 2:

 A = [2, 0, 1, 3] 
 We can divide the array into 2 chunks.
 First chunk is [2, 0, 1] and second chunk is [3].
 """
"""
Hint1 
What should be the smallest leftmost chunk ??
"""
"""
Solution Approach
Smallest leftmost possible chunk is smallest index at which A[0….i] contains all elements upto i.

We can check that if maximum of A[0…..i] is i, only then we can take it as a seperate chunk.

Find the smallest possible leftmost chunk using above idea and after that we can proceed similarily for the remaining part.

"""
"""accepted solution"""
# @param A : list of integers
# @return an integer
def solve( A):
    cnt = 0
    ma = 0
    i = 0
    for x in A:
        ma = max(ma, x)
        if ma == i: 
            cnt += 1
        i += 1
    return cnt