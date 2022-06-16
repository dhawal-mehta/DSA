"""
Shortest Distance in a Maze

Problem Description

Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.

Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.



Problem Constraints

2 <= N, M <= 100

0 <= A[i] <= 1

0 <= B[i][0], C[i][0] < N

0 <= B[i][1], C[i][1] < M



Input Format

The first argument given is the integer matrix A.

The second argument given is an array of integer B.

The third argument if an array of integer C.



Output Format

Return a single integer, the minimum distance required to reach destination



Example Input

Input 1:

A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]

Input 2:

A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]



Example Output

Output 1:

 1

Output 2:

 1



Example Explanation

Explanation 1:

 Go directly from start to destination in distance 1.

Explanation 2:

 Go directly from start to destination in distance 1.
"""
"""
Hint 1

We can observe that the ball will roll until it hits a wall. How can we use this to reach some conclusions?
We can definitely say that ball will roll only in one of 4 directions, this gives us only 4 options for each place.

"""
"""
Solution Approach

We can definitely say that ball will roll only in one of 4 directions, this gives us only 4 options for each place.
This points towards a BFS based solution. This can be written easily using starting point as source and running bfs until
queue gets empty or we reach our destiniation.

"""
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        from collections import deque
        
        de = deque()
        de.append([B[0], B[1], 0])
        visited = [ [0 for i in range(len(A[0]))] for j in range(len(A))]
        visited[B[0]][B[1]] = 1
        
        while de:
            currx, curry, d = de.popleft()
            # print(currx, curry, de)
            if currx == C[0] and curry == C[1]:
                return d

            # roll up
            upx = currx
            upy = curry
            upd = d
            while upx > 0 and A[upx-1][upy] == 0:
                upx -= 1
                upd += 1
                
            if visited[upx][upy] == 0:
                visited[upx][upy] = 1
                de.append([upx,upy,upd])


            #roll right
            rtx = currx
            rty = curry
            rtd = d
            while rty < len(A[0])-1 and A[rtx][rty+1] == 0:
                rty += 1
                rtd += 1
                
            if visited[rtx][rty] == 0:
                visited[rtx][rty] = 1
                de.append([rtx,rty,rtd])
            
            #roll down
            dwx = currx
            dwy = curry
            dwd = d
            while dwx < len(A)-1 and A[dwx+1][dwy] == 0:
                dwx += 1
                dwd += 1
                
            if visited[dwx][dwy] == 0:
                visited[dwx][dwy] = 1
                de.append([dwx,dwy,dwd])
            
            # roll left
            ltx = currx
            lty = curry
            ltd = d
            while lty > 0 and A[ltx][lty-1] == 0:
                lty -= 1
                ltd += 1
                
            if visited[ltx][lty] == 0:
                visited[ltx][lty] = 1
                de.append([ltx,lty,ltd])
                

        return -1  
            
            
        