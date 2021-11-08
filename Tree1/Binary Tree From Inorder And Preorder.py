"""
Binary Tree From Inorder And Preorder


Problem Description

Given preorder and inorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.



Problem Constraints

1 <= number of nodes <= 105


Input Format

First argument is an integer array A denoting the preorder traversal of the tree.

Second argument is an integer array B denoting the inorder traversal of the tree.



Output Format

Return the root node of the binary tree.


Example Input

Input 1:

 A = [1, 2, 3]
 B = [2, 1, 3]

Input 2:

 A = [1, 6, 2, 3]
 B = [6, 1, 3, 2]



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
First element of preorder traversal will be root. Combine this info with inorder traversal. 

How can this help you?
"""
"""
Solution Approach
Focus on the preorder traversal to begin with.
The first element in the traversal will definitely be the root.
Based on this information, can you identify the elements in the left subtree and right subtree ? ( Hint : Focus on inorder traversal and root information )

Once you do that, your problem has now been reduced to a smaller set. Now you have the inorder and preorder traversal for the left and right subtree and you need to figure them out.
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
	    
	    if A is None or B is None or len(A)!=len(B):
	        return None
	    
	    root_ele = A[0]
	    root_in_index = B.index(root_ele)
	    
	    root = TreeNode(root_ele)
	    
	    #left sub-tree
	    if root_pre_index > 0:
	        
	        left_in = B[:root_pre_index]
	        left_size = len(left_in)
	        left_pre = A[1:1+left_size]
	        if left_pre:
	            root.left = buildTree(left_pre,left_in)
	    
	    #right sub-tree
	    if root_pre_index < len(B)-1:
	        
	        right_in = B[root_pre_index+1:]
	        right_size = len(right_in)
	        right_pre = A[len(A)-right_size:]
	        if right_pre:
	            root.right = buildTree(right_pre,right_in)
	    return root