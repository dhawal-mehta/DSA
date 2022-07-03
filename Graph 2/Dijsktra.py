"""
Dijsktra


Problem Description

Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.

You have to find an integer array D of size A such that:

=> D[i] : Shortest distance form the C node to node i.

=> If node i is not reachable from C then -1.

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



Problem Constraints

1 <= A <= 1e5

0 <= B[i][0],B[i][1] < A

0 <= B[i][2] <= 1e3

0 <= C < A



Input Format

The first argument given is an integer A, representing the number of nodes.

The second argument given is the matrix B of size M x 3, where nodes B[i][0] and B[i][1] are connected with an edge of weight B[i][2].

The third argument given is an integer C.



Output Format

Return the integer array D.



Example Input

Input 1:

A = 6
B = [   [0, 4, 9]
        [3, 4, 6] 
        [1, 2, 1] 
        [2, 5, 1] 
        [2, 4, 5] 
        [0, 3, 7] 
        [0, 1, 1] 
        [4, 5, 7] 
        [0, 5, 1] ] 
C = 4

Input 2:

A = 5
B = [   [0, 3, 4]
        [2, 3, 3] 
        [0, 1, 9] 
        [3, 4, 10] 
        [1, 3, 8]  ] 
C = 4



Example Output

Output 1:

D = [7, 6, 5, 6, 0, 6]

Output 2:

D = [14, 18, 13, 10, 0]



Example Explanation

Explanation 1:

 All Paths can be considered from the node C to get shortest path

Explanation 2:

 All Paths can be considered from the node C to get shortest path
"""
"""
Hint 1

You need to use a shortest path algorithm to solve this.
What better algorithm than Dijkstra.

"""
"""
Solution Approach

Initialize a distance array of integers(denoting distance of source to node i) with infinity.
Initialize d[source]=0 (distance from source to source is 0).
Insert {d[source],source} into a min heap based on distance.
extract first element from the heap:
if this element is mark visited then again start extract top element fro heap
else mark this as vis and expore adjacent nodes of the top node of the heap:
if distance[adjacentnode]>distance[curr]+weight of the edge between curr and adjacent node
update distacne[adjacentnode] = distance[curr]+weight of the edge between curr and adjacent node
insert this node alongwith weight into minheap.

"""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        import heapq
        hp = []
        djArr = [-1]*A
        
        djArr[C] = 0
        graph = [ [] for i in range(A) ]
        s = set()
        s.add(C)
        
        for i in range(len(B)):
            graph[B[i][0]].append(i)
            graph[B[i][1]].append(i)
   
        for i in graph[C]:
            heapq.heappush(hp, (B[i][2], i, C))
    
        while hp:
            minWt, currEdge, prevNode = heapq.heappop(hp) 
            currNode = B[currEdge][0] if B[currEdge][1] == prevNode else B[currEdge][1] 

            if currNode not in s:
                s.add(currNode)
                djArr[currNode] = minWt
                
                for i in graph[currNode]:
                    nextNode = B[i][0] if B[i][1] == currNode else B[i][1]
                    if  nextNode not in s:
                        heapq.heappush(hp, (minWt + B[i][2] , i, currNode))
            
        return djArr