"""
Remove nodes from Path sum less than B


Given a binary tree with root node pointer A and an integer B. A complete path is defined as a path from the root to a leaf. The sum of all nodes on that path is defined as the sum of that path. You have to remove (prune the tree) all nodes which don't lie in any path with sum >= B.

Note: A node can be part of multiple paths. So we have to delete it only in case when all paths from it have sum less than B.


Input Format

The arguments given are root pointer A and an integer B.

Output Format

Return the root pointer after prunung the tree.

Constraints

1 <= Total number of nodos <= 100000
1 < = Nodes values <= 1000
1 <= B <= 10^9 

For Example

Input 1:

       1
      / \
     2   3
    / \  \
   3   4  5

   B = 7

Output 1:

      1
     / \
    2   3
    \    \
     4    5
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree

    def isLeaf(self,A):
        
        if A:
            
            if A.left is None and A.right is None:
                return True
            else:
                return False
        
        return False
            
    
    def util(self,A,B):
        if A:
            
            lv= self.util(A.left,B-A.val)
            rv= self.util(A.right,B-A.val)
            
            if A.val+lv<B:
                A.left = None
            if A.val+rv<B:
                A.right = None
            return A.val+max(lv,rv)
        
        return 0
    def solve(self,A,B):
        
        t= self.util(A,B)
        if t<B:
            A=None
        
        return A
        