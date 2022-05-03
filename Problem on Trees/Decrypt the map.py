"""
Decrypt the map


You have a map which consists of N points, some pairs of them are connected with a unidirectional thread (It means we can move only in the specified direction). Overall there are N - 1 thread on the map.

We need to choose a point from the map so that we can get from the chosen point to any another point on the map. For that, we may have to inverse some of thread direction (as they are unidirectional).

Tell all the points in the map which requires minimum inversion of thread direction in the given map.

Suppose we select a point P in the map which requires Q inversion of threads in order to reach all the points in the map as given above.

So you need to determine all the points for which number of inversions Q is minimum.

Input

First argument is integer N (2 ≤ N ≤ 100000) — the number of points on the map. 

Second argument is a 2D vector of N-1 rows and contains the thread  link where the 1 element is directed towards the second element of vector. A thread link is described as U,V (1 ≤ U,V ≤ N; U ≠ V). The i-th thread is oriented from U to V.You can consider points on the map indexed from 1 to N.

Output

Return a vector (sorted in ascending order) which contains all the points which give minimum inversions.

Examples:

Input

3
2 1 
2 3

Output

2

Input

4
1 4 
2 4 
3 4

Output

1 2 3

Explanation

Testcase 1-

   2
  / \
 1   3

If we select point 2 in this we do not need to do any inversions we can reach 1 and 3 with 0 inversions.
If we select point 1 in this we need to invert (2,1) thread. So we need 1 inversion.
If we select point 3 in this we need to invert (2,3) thread. So we need 1 inversion.

So answer is 2 as it needs 0 inversions.
"""

"""
Hint 1

We can see these points connected by threads as a tree.Now we need to check the edges oriented and disoriented according to the chosen node.But to check for every node it would take huge time.Now try to think if we can have all the information in 1 dfs pass by calculating levels and number of disoriented/oriented edges according to a single selected root.

"""
"""
Solution Approach

Arbitrarily root the tree at some vertex, say vertex 1. Now, all the edges are oriented either up (towards the root) or down (away from it). We will call upwards oriented edges not aligned, and downwards oriented edges as aligned. Now, with a single depth-first search, for each vertex, calculate its distance from the root (in number of edges) and the number of not aligned edges along the path to the root. Also, count the number of not aligned edges in the entire tree.

Observe that all edges outside the path from the root to vertex should become align, and those on the path should turn not align.

The number of edges that need to be flipped if a vertex is chosen is given by:

NotalignEntireTree - 2*NotalignOnPath[vert] + RootDistance[vert]

"""
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        global antiMotionEdges, totalEdge, antiEdge
        
        antiMotionEdges = 0
        totalEdge = [0]*A
        antiEdge = [0]*A
        

        
        def dfsUtil(curr, adj, visited, edges):
            global antiMotionEdges, totalEdge, antiEdge
    
            # visited[curr] = 1
            
            stk = []
            stk.append( (curr,0,0) )
            
            
            while stk:
                curr, tempTotalEdge, tempAntiEdge = stk.pop()
                
                visited[curr] = 1
                totalEdge[curr] = tempTotalEdge
                antiEdge[curr] = tempAntiEdge
                
                for i in adj[curr]:
                    
                    if visited[i] == 1:
                        continue
                    
                    if (curr, i) in edges:
                        stk.append( (i, tempTotalEdge+1, tempAntiEdge))
                    else:
                        stk.append( (i, tempTotalEdge+1, tempAntiEdge+1))
                        antiMotionEdges += 1

        adj = [ [] for i in range(A) ]
        edges = set()
        for edge in B:
            adj[edge[0] - 1].append(edge[1] - 1)
            adj[edge[1] - 1].append(edge[0] - 1)
            
            edges.add( (edge[0]-1, edge[1]-1) )

        visited = [0]*A
        dfsUtil(0, adj,  visited, edges)
        
        # print( totalEdge )
        # print( antiEdge )
        
        minReverse = antiMotionEdges
        res = []
        for i in range(A):
            minReverse = min(minReverse, antiMotionEdges - 2*antiEdge[i] + totalEdge[i])


        for i in range(A):
            if antiMotionEdges - 2*antiEdge[i] + totalEdge[i] == minReverse:
                res.append(i+1)

        
        return res