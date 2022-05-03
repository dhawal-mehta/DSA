"""
Largest BST Subtree


Problem Description

You are given a Binary Tree A with N nodes.

Write a function that returns the size of the largest subtree, which is also a Binary Search Tree (BST).

If the complete Binary Tree is BST, then return the size of the whole tree.

NOTE:

    The largest subtree is the subtree with the most number of nodes.



Problem Constraints

1 <= N <= 105



Input Format

First and only argument is an pointer to root of the binary tree A.



Output Format

Return an single integer denoting the size of the largest subtree which is also a BST.



Example Input

Input 1:

     10
    / \
   5  15
  / \   \ 
 1   8   7

Input 2:

     5
    / \
   3   8
  / \ / \
 1  4 7  9
"""
"""
Hint 1

One Approach: check whether every node is BST or not and return the maximum size subtree.
Time Complexity: O (n^2)

Improvement:
Go from bottom to top and check whether the given tree is subtree or not.

"""
"""
Solution Approach

Maintain a data structure that stores for every node the maximum value in the subtree of a node, the minimum value in the subtree of a node,
size of the subtree, size of the largest BST found in the subtree of a node, and flag to denote whether this subtree is bst or not.

Traverse the tree in a bottom-up manner.

A Tree is BST if the following is true for every node X.

    The largest value in the left subtree (of X) is smaller than the value of X.
    The smallest value in the right subtree (of X) is greater than the value of X.
    update the details of these nodes accordingly.

"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    MAX = 0
    def solve(self, A):
        
        # def util(root, start, end):
        #     if root == None:
        #         return True, 0
            
            
        #     if root.val < start or root.val > end:
        #         left, leftSize = util(root.left,-float('inf'), root.val)
        #         right, rightSize = util(root.right, root.val, float('inf') )
                
        #         print(root.val, start, end, 1+leftSize+rightSize, "vio")
        #         if  left and right:
        #             self.MAX = max(self.MAX, 1+leftSize+rightSize)        
                        
        #         return False, 0
        #     else:
        #         left, leftSize =  util(root.left, start, root.val)
        #         right, rightSize = util(root.right, root.val, end)
        #         print(root.val, start, end, 1+leftSize+rightSize, "nor")
        #         if  left and right:
        #             self.MAX = max(self.MAX, 1+leftSize+rightSize)
        #             return True, 1+leftSize+rightSize
        #         else:
        #             return False, 0
        
        # util(A, -float('inf'), float('inf'))        
        # return self.MAX
        
        #---- wrong approach as ranges will be difficult to manage 
        
        def util(root):
            if root == None:
                return True, 0
            # if root.left and root.left.val < root.val :
            
            left, leftSize = util(root.left)
            right, rightSize = util(root.right)
            
            if left and right:
                
                if ( root.left==None or (root.left != None and root.left.val <= root.val) ) and ( root.right == None or (root.right != None and root.right.val >= root.val) ):
                    # print(root.val, leftSize, rightSize, 1+leftSize+rightSize)
                    self.MAX =  max(self.MAX, 1+leftSize + rightSize)
                    # print(self.MAX)
                    
                    return True, 1+leftSize + rightSize
                else:
                    return False, 0
            
            return False, 0
        
        util(A)
        return self.MAX