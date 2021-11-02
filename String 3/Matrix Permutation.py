"""
Matrix Permutation


Given a matrix of integers A of size N x N.Find whether all rows are circular rotations of each other or not.

Return "YES",if all rows of A are circular rotations of each other, else return "NO".

Note: Rows are numbered from top to bottom and columns are numbered from left to right.


Input Format

The first argument given is the integer matrix A.

Output Format

Return "YES",if all rows of A are circular rotations of each other, else return "NO".

Constraints

1 <= N <= 1000
1 <= A[i] <= 100000

For Example

Input 1:
    A = [   [1, 2, 3]
            [3, 2, 1]
            [2, 3, 1]   ]
Output 1:
    NO

Input 2:
    A = [   [1, 2, 2, 1]
            [1, 1, 2, 2]
            [2, 1, 1, 2]    
            [1, 1, 2, 2]    ]
Output 2:
    YES
"""
"""
Solution Approach

1.Create a string of first row elements and concatenate the string with itself.Let this string be temp.
2.Traverse all remaining rows. For every row being traversed, create a string s of current row elements. If s is not a substring of temp, return false.
3.Return true.
"""
# @param A : list of list of integers
# @return a strings

def solve( A):
    
    row1 = A[0]
    
    def check(row1, row2):
        minpos = -1
        
        for i in range(len(row2)):
            if row2[i] == row1[0]:
                minpos = i
        
        if minpos == -1:
            return False
        # print(minpos)
        for i in range(len(row2)):
            if row2[ (minpos+i)%len(row2) ] != row1[i]:
                return False
        
        return True
    
    for row in range(1, len(A)):
        if not check(row1, A[row]):
            return "NO"
    
    # row1 =  [1, 2, 3]
    # row2 = [3, 2, 1]
    # print(check(row1, row2))
    
    return "YES"