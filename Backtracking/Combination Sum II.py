"""
Combination Sum II


Problem Description

Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.

Each number in A may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

Warning:

DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.

Example : itertools.combinations in python. If you do, we will disqualify your submission and give you penalty points.



Problem Constraints

1 <= N <= 20


Input Format

First argument is an integer array A denoting the collection of candidate numbers.
Second argument is an integer which represents the target number.


Output Format

Return all unique combinations in A where the candidate numbers sums to B.


Example Input

Input 1:

 A = [10, 1, 2, 7, 6, 1, 5]
 B = 8

Input 2:

 A = [2, 1, 3]
 B = 3



Example Output

Output 1:

 [ 
  [1, 1, 6 ],
  [1, 2, 5 ],
  [1, 7 ], 
  [2, 6 ] 
 ]

Output 2:

 [
  [1, 2 ],
  [3 ]
 ]



Example Explanation

Explanation 1:

 1 + 1 + 6 = 8
 1 + 2 + 5 = 8
 1 + 7 = 8
 2 + 6 = 8
 All the above combinations sum to 8 and are arranged in ascending order.

Explanation 2:

 1 + 2 = 3
 3 = 3
 All the above combinations sum to 3 and are arranged in ascending order."""

 """
 Hint 1

Think how can you use recursion with current index and target sum in order to generate all combinations.

Also, you will have to take special care of those elements which can be overcounted as they are repeated.
"""
"""
Solution Approach

Some elements can be repeated in the input set.
Make sure you iterate over the number of occurrences of those elements to make sure you are not counting the same combinations again.

Once you do that, things are fairly straightforward. Backtracking is the solution here.
You make a recursive call with the remaining sum and make sure the indices are moving forward.
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.ret:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])
    def combinationSum(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret

