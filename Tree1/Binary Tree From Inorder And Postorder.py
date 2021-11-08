"""
Binary Tree From Inorder And Postorder


Problem Description

Given inorder and postorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.



Problem Constraints

1 <= number of nodes <= 105


Input Format

First argument is an integer array A denoting the inorder traversal of the tree.

Second argument is an integer array B denoting the postorder traversal of the tree.



Output Format

Return the root node of the binary tree.


Example Input

Input 1:

 A = [2, 1, 3]
 B = [2, 3, 1]

Input 2:

 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]



Example Output

Output 1:

   1
  / \
 2   3

Output 2:

   1  
  / \
 6   2
    /
   3



Example Explanation

Explanation 1:

 Create the binary tree and return the root node of the tree.
"""
"""
Hint 1
Last element of postorder traversal will be root. Combine this info with inorder traversal. How can this help you?
"""
"""
Solution Approach
Focus on the postorder traversal to begin with.
The last element in the traversal will definitely be the root.
Based on this information, can you identify the elements in the left subtree and right subtree ? ( Hint : Focus on inorder traversal and root information )

Once you do that, your problem has now been reduced to a smaller set. Now you have the inorder and postorder traversal for the left and right subtree and you need to figure them out.
Divide and conquer.

Bonus points if you can do it without recursion.
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        
        if len(A) != len(B) or A is None or B is None:
            return None
        
        root_ele = B[-1]
        
        #Root Element
        root = TreeNode(root_ele)
        root_index_in = A.index(root_ele)
        
        #left subtree
        if root_index_in > -1:
            left_tree_in = A[:root_index_in] #A for left subTree
            left_tree_size = len(left_tree_in)
            left_tree_po = B[:left_tree_size] #B for left subTree
            if left_tree_in:
                left_sub_tree = self.buildTree(left_tree_in,left_tree_po)
                root.left = left_sub_tree
        
        #right subtree
        if root_index_in < len(A)-1:
            right_tree_in = A[root_index_in+1:] #A for right subTree
            right_tree_size = len(right_tree_in)
            po_s_in = len(B) - right_tree_size -1 
            right_tree_po = B[po_s_in:-1] #B for right subTree
            if right_tree_in:
                right_sub_tree = self.buildTree(right_tree_in,right_tree_po)
                root.right = right_sub_tree
        
        
        
        return root

