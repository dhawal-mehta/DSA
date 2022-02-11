"""
Matrix Search


Problem Description

Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than or equal to the last integer of the previous row.

Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N, M <= 1000
1 <= A[i][j], B <= 106


Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.


Output Format

Return 1 if B is present in A, else return 0.


Example Input

Input 1:

A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3

Input 2:

A = [   
      [5, 17, 100, 111]
      [119, 120, 127, 131]    
    ]
B = 3



Example Output

Output 1:

1

Output 2:

0



Example Explanation

Explanation 1:

 3 is present in the matrix at A[0][1] position so return 1.

Explanation 2:

 3 is not present in the matrix so return 0.
 """
"""
Hint 1

Look at the matrix properties carefully. Basically you are given the elements in sorted order already.

How can you exploit this property now?
"""

"""
Solution Approach

If you write down the numbers of row 1 followed by numbers in row2, row3 and so on, do you think the resulting array would be sorted ?

If yes, how do you search for a number efficiently in a sorted array ?

Just think of how the index in the array can be translated to the elements in the matrix.
For eg: Total elements : mn; m = no of rows; n = no of columns.
Indexing will go from 0 to mn - 1. Since the matrix is sorted, binary search can be applied here.
We take the mid of the total search space (initially all elements), then translate it to the indexes in the matrix
by row = int(mid / n) and col = int(mid % n) . This is valid because every row contains n elements
"""

# @param A : list of list of integers
# @param B : integer
# @return an integer
def searchMatrix(self, A, B):
    m = len(A)
    n = len(A[0])
    low = 0
    high = m * n - 1
    while(low < high):
        mid = low +( high - low + 1 ) / 2
        if(A[int(mid / n)][int(mid % n)] <= B):
            low = mid
        else:
            high = mid - 1
    
    if(A[int(low / n)][int(low % n)] == B):
        return 1
    else:
        return 0