"""
Maximum Subtree


Problem Description

You are given a tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.

You are given Q queries. In each query, you will be given a unique integer j. You are required to remove the j'th numbered edge from the tree.

This operation will divide a tree into two different trees.

For each query, once you perform the remove operation, you are asked to tell the maximum size among all the sizes of the trees present till that query.

NOTE:

1) Once an edge is removed, it will be considered removed for all the further queries.

2) It is guaranteed that each edge will be pointing to exactly two different nodes of the tree.

3) Edges are numbered from 1 to A-1. Please read the input format for more clarification.



Problem Constraints

2 <= A <= 105

1 <= B[i], C[i] <= A

1 <= D[i], Q <= A-1



Input Format

The first argument is an integer A denoting the number of nodes.

The second and third arguments are the integer arrays B and C where for each i (0 <= i < A-1), i denotes the (i+1)th edge and B[i] and C[i] are the nodes connected by it.

The fourth argument is an integer array D of distinct elements where D[i] denotes the number of the edge to be removed for the ith query.



Output Format

Return an array of answers.


Example Input

Input 1:

 A = 5
 B = [1, 3, 3, 5]
 C = [3, 2, 4, 1]
 D = [1, 3]

Input 2:

 A = 2
 B = [1]
 C = [2]
 D = [1]



Example Output

Output 1:

 [3, 2]

Output 2:

 [1]



Example Explanation

Explanation 1:

 Initial tree:
        1
       / \            
      3   5
     /\
    2  4

    Query 1: 
    Remove edge number 1: 1-3
        1
      /  \ 
      3   5
     /\
    2  4

    Obtained Trees:-
        Node 2, Node 3, Node 4 => Size 3
        Node 1, Node 5 => Size 2

    Max Size = 3

    Query 2: 
    Remove edge number 3: 3-4
         1
       /  \ 
      3   5
     / \
    2  4
    Obtained Trees:-
        Node 2, Node 3 => Size = 2
        Node 4 => Size = 1
        Node 1, Node 5 => Size = 2

    Max Size = 2


Explanation 2:

 2 trees of size 1 are left.
"""
"""
Hint 1

Breaking trees seems hard, However you can unite trees by DSU.
Can you use this to think up a solution??

"""
"""
Solution Approach

We should iterate over the queries one by one in reverse fashion.
We initially have a broken down tree which can be united using DSU
and max size of a subtree can be reported.
This is to be done for all queries and corresponding parts should be united.
Thus we can return the answer for each query easily.

"""
N = 10**5 + 10
sz = [0 for i in range(N)]
par = [0 for i in range(N)]
edge = [[0 for i in range(2)] for j in range(N)]

n = 0
k = [0 for i in range(N)]
mx = 0
removed = [0 for i in range(N)]

def root(x):
    global par
    x1 = x 
    while par[x] != x:
        x = par[x]
    par[x1] = x 
    return x 

def unite(u, v):
    global sz, mx
    if u == v:
        return 
    if sz[u] < sz[v]:
        u, v, = v, u 
    par[v] = u 
    sz[u] += sz[v]
    mx = max(mx, sz[u])
    
class Solution:
    def solve(self, A, B, C, D):
        global N, sz, par, edge, n, k, mx, removed
        removed = [0 for i in range(N)]
        n = A
        
        mx = 1
        
        for i in range(n - 1):
            edge[i][0] = B[i]
            edge[i][1] = C[i]
        # print(edge[:A-1])
        # for i in range(n - 1):
            
        q = len(D)
        
        for i in range(q):
            removed[D[i] - 1] = 1
            

        
        for i in range(1, n + 1):
            sz[i] = 1
            par[i] = i 
        
        # print(removed[:A-1])
        # print(sz[:A+1])
        # print(par[:A+1])
        
        for i in range(n - 1):
            if removed[i]:
                continue
            u = root(edge[i][0])
            v = root(edge[i][1])
            unite(u, v)
        
        # print( sz[:A+1] )
        # print( par[:A+1] )    
        res = [0 for i in range(q)]
        for i in range(q-1, -1, -1):
            res[i] = mx 
            u = root(edge[D[i] - 1][0])
            v = root(edge[D[i] - 1][1])
            unite(u, v)
            
        return res