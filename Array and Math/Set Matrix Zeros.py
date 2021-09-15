"""Set Matrix Zeros

Problem Description
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.

Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

Input Format:

The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.

Output Format:

Return a 2-d matrix that satisfies the given conditions.

Constraints:

1 <= N, M <= 1000
0 <= A[i][j] <= 1

Examples:

Input 1:
    [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]

Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]

Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
"""
"""
Hint 1

Let the matrix be of size M * N.
A simplistic solution is creating a copy of the matrix and working on top of it. Additional space complexity will be O(M * N). Obviously, we expect you to do better.

The next better solution uses additional space complexity of O(M+N). It works on the phenomenon that for every row, you only need to find if there is any element in the row which is 0.

Similarly so for every column. Once that is known, all the rows with 0 can be set completely as 0 (and the same for columns).

The next better solution uses constant additional space.
Can you think of a solution using constant additional space ? Think in terms of re-using the space in first row and first column.

"""
"""
Small explanation :

We use the first row and column in the matrix to store what we need to store in step 2. The trick is in using the first row and column to store the information.
Then we need to know whether or not to set the first row and column to zeroes. So, we use two boolean to store that information.

Detailed explanation :

So, you have 2 additional variables ( lets say R and C ). Firstly convince yourself that if in the original array, if any of the value in the first row was 0, the whole row will be 0. So R stores just that information ( whether any of the value in the row was 0 ). Now, if R = 0, your job is simple. In the end, mark every element in the first row as 0. If R = 1, then leave the row as it is ( with each cell storing whether their corresponding column has any zeroes ).
Things work very similarily for columns.

Let me demonstrate using an example.
Lets say the array was

[ 
1 1 1
0 1 1
1 0 1
]

Now, R = 1 as everything in row 1 = 1. C = 0, as second element in first column is 0.
Now, using first row and first column to store value about their respective columns and rows ( For the first row, column i stores if all the value in column i are 1. For the first column, row i stores if all the values in row i are 1. We leave 0,0 unassigned )

[
X 0 1
0 . .
0 . .
] 

is what you get.

Now, for any entry which is not in first row or first column, entry (r,c) is 1, if its corresponding column entry in first row is 1 and corresponding row entry in first column is 1.

[
0 0 1
0 0 0 
0 0 0 
]

"""
# @param A : list of list of integers
# @return the same list modified
def setZeroes(self, A):
    rowFlag = False
    colFlag = False
    m = len(A)
    if m == 0:
        return A
    n = len(A[0])
    if n == 0:
        return A
    for i in range(n):
        if A[0][i] == 0:
            rowFlag = True
            break
    for i in range(m):
        if A[i][0] == 0:
            colFlag = True
            break
    for i in range(1,m):
        for j in range(1,n):
            if A[i][j] == 0:
                A[0][j] = 0
                A[i][0] = 0
    
    for i in range(1,m):
        for j in range(1,n):
            if A[0][j] == 0 or A[i][0] == 0:
                A[i][j] = 0
    if rowFlag:
        for i in range(n):
            A[0][i] = 0
    if colFlag:
        for i in range(m):
            A[i][0] = 0
    return