"""
Commutable Islands

Problem Description

There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.



Problem Constraints

1 <= A, M <= 6*104

1 <= B[i][0], B[i][1] <= A

1 <= B[i][2] <= 103



Input Format

The first argument contains an integer, A, representing the number of islands.

The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].



Output Format

Return an integer representing the minimal cost required.



Example Input

Input 1:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 4]
        [1, 4, 3]
        [4, 3, 2]
        [1, 3, 10]  ]

Input 2:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 2]
        [3, 4, 4]
        [1, 4, 3]   ]



Example Output

Output 1:

 6

Output 2:

 6



Example Explanation

Explanation 1:

 We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.

Explanation 2:

 We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.
"""

"""
Hint 1

Hint : Try to think in terms of graph.
Can we make a graph out of the given data and use some graph algorithms?

"""
"""
Solution Approach

We can assume islands as the vertex points and bridges as the edges and can construct a graph with the the help of them. After constructing the graph, the problem boils down to finding a subset of edges which helps in connecting vertices in a single connected component such that the sum of their edge weights is as minimum as possible.

Now since the problem is clear to you, can you think of any graph theory algorithms related to this?

Well the answer to this problem is the classic minimum spanning tree algorithm. In this algorithm we aim at finding subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

There are many algorithms for finding minimum spanning tree of a graph. Some of them are Kruskal’s algorithm, Prim’s algorithm etc.

    Kruskal’s algorithm in detail can be found at : https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    Prim’s algorithm in detail can be found at : https://en.wikipedia.org/wiki/Prim%27s_algorithm

Now, can you code this?

"""
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        parent = [i for i in range(A) ]
        size = [ 1 for i in range(A) ]
        
        B = B.sort(key= lambda x : x[2])
        
        def getParent(N):
            p = N
            while parent[p] != p:
                p = parent[p]
            return p
        
        s = set()
        res = 0
        for src, dest, wt in B:
            
            srcP = getParent( src )
            destP = getParent( dest )
            
            if srcP != destP:
                if size[srcP] > size[destP]:
                    parent[destP] = srcP
                    size[srcP] += size[destP]
                else:
                    parent[srcP] = destP
                    size[destP] += size[srcP]                    
                
                res += wt
                    
        return res
