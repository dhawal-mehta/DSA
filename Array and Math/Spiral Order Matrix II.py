"""Spiral Order Matrix II

Problem Description

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.


Problem Constraints

1 <= A <= 1000


Input Format

First and only argument is integer A



Output Format

Return a 2-D matrix which consists of the elements in spiral order.


Example Input

Input 1:

1

Input 2:

2



Example Output

Output 1:

[ [1] ]

Output 2:

[ [1, 2], [4, 3] ]



Example Explanation

Explanation 1:

 
Only 1 is to be arranged.

Explanation 2:

1 --> 2
      |
      |
4<--- 3
"""

"""
Hint 1

This is more of a simulation problem.

Try to figure out when to change direction and when to terminate the algorithm.

"""

"""
Solution approach

This is more of a simulation problem.

You need to maintain state indicating which direction you are traversing to ( left to right, right to left, top to down, down to top ) and then know when to change the directions.

Note that in each direction, either row or column remains constant.

Based on the constant row or column, you can predict when to change the direction.

"""
# @param A : integer
# @return a list of list of integers
def generateMatrix( A):
    row_top_left =0
    col_top_left =0
    
    row_top_right =0
    col_top_right =A-1
    
    row_bot_left =A-1
    col_bot_left =0
    
    row_bot_right =A-1
    col_bot_right =A-1
    
    
    res = [ [0]*A for i in range(A) ]
    
    num = 1
    
    while  num < A*A:
        
        for i in range(col_top_left,col_top_right):
            res[row_top_left][i] = num
            num+= 1
        
        for i in range(row_top_right,row_bot_right):
            res[i][col_top_right] = num
            num+= 1
        
        for i in range(col_bot_right, col_bot_left,-1):
            res[row_bot_right][i] = num
            num+= 1
            
        for i in range(row_bot_left,row_top_left, -1):
            res[i][col_bot_left] = num
            num+= 1
        
        
        row_top_left +=1
        col_top_left +=1
        
        row_top_right +=1
        col_top_right -=1
        
        row_bot_left -=1
        col_bot_left += 1
        
        row_bot_right -= 1
        col_bot_right -= 1
        
    if A%2 == 1:
        res[A//2][A//2] = A*A
    
    # print(res)
    
    return res
