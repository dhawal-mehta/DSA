"""
Black Shapes

Problem Description

Given character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)



Problem Constraints

1 <= |A|,|A[0]| <= 1000

A[i][j] = 'X' or 'O'



Input Format

The First and only argument is character matrix A.


Output Format

Return a single integer denoting number of black shapes.


Example Input

Input 1:

 A = [ [X, X, X], [X, X, X], [X, X, X] ]

Input 2:

 A = [ [X, O], [O, X] ]



Example Output

Output 1:

 1

Output 2:

 2



Example Explanation

Explanation 1:

 All X's belong to single shapes

Explanation 2:

 Both X's belong to different shapes
"""
"""
Hint 1

You need to find number of different connected components here. Any graph traversal algorithm can do this.
You can always use both DFS and BFS to see the working of both of these traversal algorithms.
They will always help you solve such type of problems.

"""
"""
Solution Approach

Simple graph traversal approach:

Answer := 0
Loop i = 1 to N :
    Loop j = 1 to M:
          IF MATRIX at i, j equal to 'X' and not visited:
                 BFS/DFS to mark the connected area as visited
                 update Answer
    EndLoop
EndLoop

return Answer
You can always use both DFS and BFS to see the working of both of these traversal algorithms.
They will always help you solve such type of problems.

"""
class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        from collections import deque
        
        def util(x ,y ):
            de = deque()
            de.append([x ,y])
            
            while de:
                x ,y = de.popleft()
                if x > 0 and A[x -1][y] == 'X':
                    A[x -1][y] += 'O'
                    de.append([x -1,y])
                    
                if x < len(A)-1 and A[x +1][y] == 'X':
                    A[x +1][y] += 'O'
                    de.append([x +1,y])
                    
                if y > 0 and A[x ][y-1] == 'X':
                    A[x ][y-1] += 'O'
                    de.append([x ,y-1])
                    
                if y < len(A[0])-1 and A[x ][y+1] == 'X':
                    A[x][y+1] += 'O'
                    de.append([x ,y+1])   
                    
        res =0 
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 'X' :
                    res += 1
                    util(i,j)
        
        return res
             