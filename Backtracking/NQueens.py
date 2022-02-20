"""
NQueens


Problem Description

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer A, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
The final list should be generated in such a way that the indices of the queens in each list should be in reverse lexicographical order.



Problem Constraints

1 <= A <= 10


Input Format

First argument is an integer n denoting the size of chessboard


Output Format

Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.


Example Input

Input 1:

A = 4

Input 2:

A = 1



Example Output

Output 1:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Output 1:

[
 [Q]
]



Example Explanation

Explanation 1:

There exist only two distinct solutions to the 4-queens puzzle:

Explanation 1:

There exist only one distinct solutions to the 1-queens puzzle:
"""
"""
Hint 1

Unfortunately, there is no magic trick to solve this problem. This is more of a bruteforce problem. A more intelligent bruteforce.

Think recursively. Store which places are occupied already and move on to next row and fill in either of the available positions and go on.
"""
"""
Solution Approach

Notes :
1) There can exactly be one queen per row. Otherwise the 2 queens in the row would collide. If you miss out on a row, there cannot be N queens on the board.
2) Every column needs to have exactly one queen.
3) The left diagonal cannot have more than one queen ( Unique (row + col) )
4) The right diagonal cannot have more than one queen ( Unique (row - col) )

We can start placing a queen per row. When placing a queen on a row, col, we need to check if the position is available based on what we have already placed. Then we move to the next row.
"""
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        n=A
        stack, res = [[(0, i)] for i in range(n)], []
        while stack:
            board = stack.pop()
            row = len(board)
            if row == n:
                res.append([''.join('Q' if i == c else '.' for i in range(n))
                            for r, c in board])
            for col in range(n):
                if all(col != c and abs(row-r) != abs(col-c)for r, c in board):
                    stack.append(board+[(row, col)])
        return res
