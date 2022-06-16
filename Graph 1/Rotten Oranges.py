"""
Rotten Oranges


Problem Description

Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.



Problem Constraints

1 <= N, M <= 1000

0 <= A[i][j] <= 2



Input Format

The first argument given is the integer matrix A.



Output Format

Return the minimum number of minutes that must elapse until no cell has a fresh orange.

If this is impossible, return -1 instead.



Example Input

Input 1:

A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]

Input 2:

 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]



Example Output

Output 1:

 4

Output 2:

 -1



Example Explanation

Explanation 1:

 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)

Explanation 2:

 Task is impossible
"""
"""
Hint 1

Every turn, the rotting spreads from each rotting orange to other adjacent oranges.
Initially, the rotten oranges have ‘depth’ 0, and every time they rot a neighbor,
the neighbors have 1 more depth. We want to know the largest possible depth.
Think of this as possible solution

"""
"""
Solution Approach

Every turn, the rotting spreads from each rotting orange to other adjacent oranges.
Initially, the rotten oranges have ‘depth’ 0, and every time they rot a neighbor,
the neighbors have 1 more depth. We want to know the largest possible depth.

Use multi-source BFS to achieve this with all cells containing rotten oranges as starting nodes.
At the end check if there are fresh oranges left or not.

"""
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        import collections
        d = collections.deque([])
        
        # d.append(2)
        # d.appendleft(3)
        count_1 = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 2:
                    d.append([i,j,0])
                    A[i][j] = 0
                if A[i][j] == 1:
                    count_1 += 1
        
        res = 0
        curr_count_1 = 0
        while d:
            curri, currj, time = d.popleft()
            if curri > 0 and A[curri-1][currj] == 1:
                res = max(res, time+1)
                A[curri-1][currj] = 0
                d.append([curri-1,currj, time+1])
                curr_count_1 += 1
                
            if curri < len(A)-1 and A[curri+1][currj] == 1:
                res = max(res, time+1)
                A[curri+1][currj] = 0
                d.append([curri+1 ,currj, time+1])
                curr_count_1 += 1

            if currj > 0 and A[curri][currj-1] == 1:
                res = max(res, time+1)
                A[curri][currj-1] = 0
                d.append([curri,currj-1, time+1])
                curr_count_1 += 1
                
            if currj < len(A[0])-1 and A[curri][currj+1] == 1:
                res = max(res, time+1)
                A[curri][currj+1] = 0
                d.append([curri,currj+1, time+1])                
                curr_count_1 += 1        
        
        
        
        # print(d)
        
        return res if curr_count_1 == count_1 else -1 