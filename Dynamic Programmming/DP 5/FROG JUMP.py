"""
FROG JUMP


A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list A of size N giving stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
Input Format

The first and olnly argument given is the integer array A.

Output Format

Return 0 if it is not possible to land on last stone, else return 1

Constraints

2 <= N <= 1000
1 <= A[i] <= 1000000

For Example

Input 1:
    A = [0,1,3,5,6,8,12,17]
Output 1:
    1
Explaination:
    There are a total of 8 stones.
    The first stone at the 0th unit, second stone at the 1st unit,
    third stone at the 3rd unit, and so on...
    The last stone at the 17th unit.

    Return true. The frog can jump to the last stone by jumping 
    1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
    2 units to the 4th stone, then 3 units to the 6th stone, 
    4 units to the 7th stone, and 5 units to the 8th stone.

Input 2:
    A = [0,1,2,3,4,8,9,11]
Output 2:
    0
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        dp = [ set() for i in range(len(A)) ]
        
        dp[1].add(2)
        dp[1].add(3)
        # print(dp)
        for i in range(2, len(A)):
            for j in range(1, i):
                if A[i] in dp[j]:
                    dp[i].add(A[i] + A[i] - A[j] - 1)
                    dp[i].add(A[i] + A[i] - A[j])
                    dp[i].add(A[i] + A[i] - A[j] + 1)
            if len(dp[i]) == 0:
                return 0
        # print(dp)
        
        return 1