"""Maximum Depth

Problem Description

Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.

You are given Q queries. In each query, you will be given two integers L and X. Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X.

Answer to the query is the smallest possible value or -1, if all the values at the required level are smaller than X.

NOTE:

Level and Depth of the root is considered as 0.
It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
Please read the input format for more clarification.


Problem Constraints

2 <= A, Q(size of array E and F) <= 105

1 <= B[i], C[i] <= A

1 <= D[i], E[i], F[i] <= 106



Input Format

The first argument is an integer A denoting the number of nodes.

The second and third arguments are the integer arrays B and C where for each i (0 <= i < A-1), B[i] and C[i] are the nodes connected by an edge.

The fourth argument is an integer array D, where D[i] denotes the value of the (i+1)th node

The fifth and sixth arguments are the integer arrays E and F where for each i (0 <= i < Q), E[i] denotes L and F[i] denotes X for ith query.



Output Format

Return an array of integers where the ith element denotes the answer to ith query.


Example Input

Input 1:

 A = 5
 B = [1, 4, 3, 1]
 C = [5, 2, 4, 4]
 D = [7, 38, 27, 37, 1]
 E = [1, 1, 2]
 F = [32, 18, 26]

Input 2:

 A = 3
 B = [1, 2]
 C = [3, 1]
 D = [7, 15, 27]
 E = [1, 10, 1]
 F = [29, 6, 26]



Example Output

Output 1:

 [37, 37, 27]

Output 2:

 [-1, 7, 27]



Example Explanation

Explanation 1:

      1[7]
     /    \
   5[1]  4[37]
        /    \
       2[38]  3[27]

 Query 1: 
    L = 1, X = 32
    Nodes for level 1 are 5, 4
    Value of Node 5 = 1 < 32
    Value of Node 4 = 37 >= 32
    Ans = 37

Explanation 2:

      1[7]
     /    \
   2[15]  3[27]

 Query 1: 
    L = 1, X = 6
    Nodes for level 1 are 2, 3 having value 15 and 27 respectively.
    Answer = -1 (Since no node is greater or equal to 29).
 Query 1: 
    L = 10 % 2 = 0, X = 6
    Nodes for level 0 is 1 having value 7.
    Answer = 7.     
"""
"""
Hint 1

Can we use binary search for nodes at a particular level?
"""
"""
Solution Approach

Main idea is to maintain list of nodes at every different level.

Can we do that with dfs or bfs?

To maintain the list, Call dfs from the root of tree(1) and insert the node at in the list at particularr level.

For each query, Use binary search to find the required value at a particular level.

If there is no value present which is greater or equal to x, output -1.
"""
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    

            
    def solve(self, A, B, C, D, E, F):
        global maxdepth, level
        adj = [[] for i in range(A+1)]
        level= [[] for i in range(A+1)]
        
        maxdepth = 0
        
        def dfs( prev ,node ,d):
            global maxdepth
            
            level[d].append(D[node-1])
            maxdepth = max(maxdepth, d)
            
            for i in adj[node]:
                if i == prev:
                    continue
                dfs(node, i ,d+1)
        
        for i in range(A-1):
            adj[B[i]].append(C[i])
            adj[C[i]].append(B[i])
        
        # print(adj)        
        dfs(1, 1, 0)
        # print(level, maxdepth)
        
        for i in range(maxdepth + 1):
            level[i].sort()
        
        res = []
        
        def bisect(start, end, L, num):
            if start == end:
                return start if level[L][start] >= num else start+1
            
            mid = (start + end)//2
            
            if level[L][mid] >= num and ( mid == 0 or level[L][mid-1] < num):
                return mid
                
            elif level[L][mid] < num: #right
                return bisect(mid+1, end, L, num)
                
            else: #left
                return bisect(start, mid-1, L, num )
        
        for i in range(len(E)):
            
            L =  E[i]%(maxdepth+1)
            
            # print(L)
            
            temp = bisect(0, len(level[L])-1, L, F[i])
            
            if temp == len(level[L]):
                res.append(-1)
            else:
                res.append(level[L][temp])


        return res