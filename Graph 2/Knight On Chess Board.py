"""
Knight On Chess Board


Problem Description

Given any source point, (C, D) and destination point, (E, F) on a chess board of size A x B, we need to find whether Knight can move to the destination or not.

The above figure details the movements for a knight ( 8 possibilities ).

If yes, then what would be the minimum number of steps for the knight to move to the said point. If knight can not move from the source point to the destination point, then return -1.

NOTE: A knight cannot go out of the board.



Problem Constraints

1 <= A, B <= 500



Input Format

The first argument of input contains an integer A.
The second argument of input contains an integer B.
The third argument of input contains an integer C.
The fourth argument of input contains an integer D.
The fifth argument of input contains an integer E.
The sixth argument of input contains an integer F.



Output Format

If it is possible to reach the destination point, return the minimum number of moves.
Else return -1.



Example Input

Input 1:

 A = 8
 B = 8
 C = 1
 D = 1
 E = 8
 F = 8

Input 2:

 A = 2
 B = 4
 C = 2
 D = 1
 E = 4
 F = 4



Example Output

Output 1:

 6

Output 2:

 -1



Example Explanation

Explanation 1:

 The size of the chessboard is 8x8, the knight is initially at (1, 1) and the knight wants to reach position (8, 8).
 The minimum number of moves required for this is 6.

Explanation 2:

 It is not possible to move knight to position (4, 4) from (2, 1)
"""
"""
Hint 1

Assume this problem as searching in graph where each block of chess board is vertex.
How would you define edges in such a graph ?
When can you travel from vertex i to vertex j ?

Once you have the graph, then it reduces to finding the shortest path in an unweighted graph.
How do you find the shortest path in an unweighted graph ?

"""
"""
Solution Approach

A knight can move to 8 positions from (x,y). 

(x, y) -> 
    (x + 2, y + 1)  
    (x + 2, y - 1)
    (x - 2, y + 1)
    (x - 2, y - 1)
    (x + 1, y + 2)
    (x + 1, y - 2)
    (x - 1, y + 2)
    (x - 1, y - 2)

Corresponding to the knight's move, we can define edges. 
(x,y) will have an edge to the 8 neighbors defined above. 

To find the shortest path, we just run a plain BFS. 

"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        
        from collections import deque
        de = deque()
        de.append([C,D, 0])
        
        res = float('inf')
        s = set()
        s.add((C,D))
        
        while de:
            currR, currC, wt = de.popleft()
            if currR == E and currC == F:
                res = min(res , wt)
                
            else:
                if currR + 2 <= A:
                    if currC + 1 <= B and (currR+2, currC+1) not in s:
                        s.add((currR+2,currC+1))
                        de.append( [currR+2, currC+1, wt+1] )
                    
                    if currC - 1 >= 1 and (currR+2, currC-1) not in s:
                        s.add((currR+2, currC-1))
                        de.append( [currR+2, currC-1, wt+1] )

                if currR - 2 >= 1:
                    if currC + 1 <= B and (currR-2, currC+1) not in s:
                        s.add((currR-2,currC+1))
                        de.append( [currR-2, currC+1, wt+1] )
                    
                    if currC - 1 >= 1 and (currR-2, currC-1) not in s:
                        s.add((currR-2, currC-1))
                        de.append( [currR-2, currC-1, wt+1] )

                if currR + 1<= A:
                    if currC + 2 <= B and (currR+1, currC+2) not in s:
                        s.add((currR+1,currC+2))
                        de.append( [currR+1, currC+2, wt+1] )
                    
                    if currC - 2 >= 1 and (currR+1, currC-2) not in s:
                        s.add((currR+1, currC-2))
                        de.append( [currR+1, currC-2, wt+1] )

                if currR - 1 >= 1:
                    if currC + 2 <= B and (currR-1, currC+2) not in s:
                        s.add((currR-1,currC+2))
                        de.append( [currR-1, currC+2, wt+1] )
                    
                    if currC - 2 >= 1 and (currR-1, currC-2) not in s:
                        s.add((currR-1, currC-2))
                        de.append( [currR-1, currC-2, wt+1] )
             
        return res if res != float('inf') else -1       
                
                
            