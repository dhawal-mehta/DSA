"""
Number of Squareful Arrays


Problem Description

Given an array of integers A, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Find and return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].



Problem Constraints

1 <= length of the array <= 12

1 <= A[i] <= 109



Input Format

The only argument given is the integer array A.


Output Format

Return the number of permutations of A that are squareful.


Example Input

Input 1:

 A = [2, 2, 2]

Input 2:

 A = [1, 17, 8]



Example Output

Output 1:

 1

Output 2:

 2



Example Explanation

Explanation 1:

 Only permutation is [2, 2, 2], the sum of adjacent element is 4 and 4 and both are perfect square.

Explanation 2:

 Permutation are [1, 8, 17] and [17, 8, 1]."""

"""
Hint 1

Construct a graph where an edge from i to j exists if A[i] + A[j] is a perfect square.

Our goal is to investigate Hamiltonian paths of this graph: paths that visit all the nodes exactly once.
"""
"""
Solution Approach

Construct a graph where an edge from i to j exists if A[i] + A[j] is a perfect square.

Our goal is to investigate Hamiltonian paths of this graph: paths that visit all the nodes exactly once.

Let’s keep a current count of what values of nodes are left to visit, and a count todo of how many nodes left to visit.

From each node, we can explore all neighboring nodes (by value, which reduces the complexity).

Alternate solution that is explained in the video:
We can also go through all permuations and then check which ones satisfy the given condition in the problem.

But since this will be very time infefficient, we can instead only permute further when we are sure that the current
permutation will lead to the answe
"""


import collections

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        if N == 1:
            return 0
        count = collections.Counter(A)
        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if int((x+y)**.5 + 0.5) ** 2 == x + y:
                    graph[x].append(y)
        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans
        return sum(dfs(x, len(A) - 1) for x in count)

