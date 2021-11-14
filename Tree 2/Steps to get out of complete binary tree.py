"""
Steps to get out of complete binary tree


You are given two integers A and B. A describes the number of nodes in complete binary tree. You are B steps away from your destination in the worst case.

Initially, you can be at:

    The root node of the tree and can only move bottom of the tree.

    Any leaf node of the tree and can only move up the tree.

Find and return an array of integers C of size 2 where

C[0]: The number of nodes which are at B steps from the root, i.e. the number of nodes such that, starting at that root, you have to take B steps downwards to reach the node.

C[1]: The number of nodes such that the maximum distance from the node to any leaf in the subtree of the node is B.

NOTE: A Complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.


Input Format

The only argument given is the integer array A.

Output Format

Return an array of integers C.

Constraints

1 <= A <= 10^9
0 <= B <= 100

For Example

Input 1:
    A = 10
    B = 0
Output 1:
    C = [1, 5]
    distance is 0:
    from root : only 1 node(root itself)
    from leaf nodes: 5 nodes (all 5 leaf nodes)

Input 2:
    A = 10
    B = 2
Output 2:
    C = [4, 1]
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):  

        fromroot = [0]*100
        fromleaf = [0]*100
        temp=A
        level=0
        ans=[]
        while(temp):
            fromroot[level] =  min(temp,(1<<level)) 
            temp -= min(temp, (1<<level) )
            level+=1
        

        level-= 1
        left = (1<<level) - fromroot[level]

        for  i in range(0,level+1):
            fromleaf[i] = fromroot[level-i]

        # print(fromroot[:6])
        # print(fromleaf[:6])

        for i in range(0,level+1):
            fromleaf[i+1] -= (left>>1)
            fromleaf[i] += (left>>1)
            left >>= 1
        

        if(B>level):
            ans.append(0);
            ans.append(0);
        
        elif(A==1):
            ans.append(1);
            ans.append(1);
        
        else :
            ans.append(fromroot[B]);
            ans.append(fromleaf[B]);
        

        return ans