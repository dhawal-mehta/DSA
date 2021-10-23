"""
Valid Sudoku


Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.

The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]

A partially filled sudoku which is valid.

    Note:

        A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
"""
Solution Approach

Very simple simulation problem. Just need to keep track of the digits seen in every row, every column and every block as defined in the rules.
Whenever you encounter a digit already seen, you know the sudoku is not valid.

Note that this problem will get very complicated if you were to determine if the sudoku was solvable.
"""
# @param A : tuple of strings
# @return an integer
def isValidSudoku( A):
    sudoku = [[0]*9 for i in range(9) ]
    
    for i in range( len(A) ):
        for j in range( len(A[i]) ):
            if A[i][j] != ".":
                sudoku[i][j] = int(A[i][j])
    
    for row in range(9):
        rowSet = set()
        colSet = set()
        for col in range(9):
            if sudoku[row][col] > 0: 
                if sudoku[row][col] in rowSet:
                    return 0
                else:
                    rowSet.add( sudoku[row][col] )
            if sudoku[col][row] > 0:
                if sudoku[col][row] in colSet:
                    return 0
                else:
                    colSet.add(sudoku[col][row])
    
    for tileRow in range(3):
        for tileCol in range(3):
            i = tileRow*3
            j = tileCol*3
            prev = set()
            for tilei in range(tileRow, tileRow+3):
                for tilej in range(tileCol, tileCol+3):
                    if sudoku[tilei][tilej] > 0:
                        if sudoku[tilei][tilej] in prev:
                            return 0
                        else:
                            prev.add( sudoku[tilei][tilej] )
    # print(sudoku)
                    
    return 1
            