"""Another BFS


Problem Description

Given a weighted undirected graph having A nodes, a source node C and destination node D.

Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.

You are expected to do it in Time Complexity of O(A + M).

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



Problem Constraints

1 <= A <= 105

0 <= B[i][0], B[i][1] < A

1 <= B[i][2] <= 2

0 <= C < A

0 <= D < A



Input Format

The first argument given is an integer A, representing the number of nodes.

The second argument given is the matrix B, where B[i][0] and B[i][1] are connected through an edge of weight B[i][2].

The third argument given is an integer C, representing the source node.

The fourth argument is an integer D, representing the destination node.

Note: B[i][2] will be either 1 or 2.



Output Format

Return the shortest distance from C to D. If it is impossible to reach node D from C then return -1.


Example Input

Input 1:

 
A = 6
B = [   [2, 5, 1]
        [1, 3, 1] 
        [0, 5, 2] 
        [0, 2, 2] 
        [1, 4, 1] 
        [0, 1, 1] ] 
C = 3
D = 2

Input 2:

A = 2
B = [   [0, 1, 1]
    ] 
C = 0
D = 1



Example Output

Output 1:

 4

Output 2:

 1



Example Explanation

Explanation 1:

The path to be followed will be:
    3 -> 1 (Edge weight : 1)
    1 -> 0 (Edge weight : 1)
    0 -> 2 (Edge weight : 2)
Total length of path = 1 + 1 + 2 = 4.

Explanation 2:

 Path will be 0-> 1.
"""
"""
Hint 1

BFS can be use for finding shortest path between destination and source by modifying the original graph.
A bfs would work if all edges have same weight.
So for each edge of weight 2 insert a dummy node between them.
After modifying the graph you can apply bfs to find the shortest path from source to destination in O(A+M) time because all edges have same weight now.

"""
"""
character backgroundcharacter
Solution Approach

BFS can be use for finding shortest path between destination and source by modifying the original graph.
A bfs would work if all edges have same weight.
So for each edge of weight 2 insert a dummy node between them.
After modifying the graph you can apply bfs to find the shortest path from source to destination in O(A+M) time because all edges have same weight now.

"""
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        from collections import deque
        graph = [ [] for i in range(A) ]
        
        for i in range(len(B)):
            graph[B[i][0]].append(i)
            graph[B[i][1]].append(i)
        
        de = deque()
        de.append([C, 0, -1])
        res = float('inf')
        s = {}
        s[C] = 0
        
        while de:
            currNode, Wt, prevNode = de.popleft()
            # if currNode in s
            s[currNode] = Wt
            
            if currNode == D:
                res = min(res, Wt)
            
            for edg in graph[currNode]:
                nextNode = B[edg][0] if B[edg][0] != currNode else B[edg][1]
                
                if nextNode != prevNode and (nextNode not in s or s[nextNode] > Wt+B[edg][2]):
                    # and nextNode not in s:
                    de.append([nextNode, Wt+B[edg][2], currNode])
                    

        
        return res if res != float('inf') else -1