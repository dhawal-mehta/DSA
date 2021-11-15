"""
Identical Binary Trees

Problem Description

Given two binary trees, check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.



Problem Constraints

1 <= number of nodes <= 105


Input Format

First argument is a root node of first tree, A.

Second argument is a root node of second tree, B.



Output Format

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.


Example Input

Input 1:

   1       1
  / \     / \
 2   3   2   3

Input 2:

   1       1
  / \     / \
 2   3   3   3



Example Output

Output 1:

 1

Output 2:

 0



Example Explanation

Explanation 1:

 Both trees are structurally identical and the nodes have the same value.

Explanation 2:

 Value of left child of the tree is different."""
"""
Hint 1

Think recursively.

Call each left and right child simultaneously and check that both are same or not.
"""
"""
Hint 1

Think recursively.

Call each left and right child simultaneously and check that both are same or not.
"""
"""
Solution Approach

When are the 2 trees the same ?
When the root values are the same, and left subtree of both trees are same, and right subtree of both trees are the same.

Can you think of very easy recursive solution based on the above fact ?

"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
# 	def check(self,A, B):
	   
# 	   if A.left == None and A.right == None and B.left == None and B.right == None and A.val == B.val:
# 	       return True
	   
# 	   L = False
# 	   R = False
	   
# 	   if A.left and B.left:
# 	       L = self.check(A.left, B.left)
# 	   elif A.left == None and B.left == None:
# 	       L = True
# 	   #else:
# 	   #    return False
	       
# 	   if A.right and B.right:
# 	       R = self.check(A.right, B.right)
# 	   elif A.right == None and B.right == None:
# 	       R = True
# 	   #else:
# 	   #    return False
	   
# 	   return (A.val == B.val) and L and R
	   
    def check(self, A,B):
        if A==None and B== None:
            return True
        if A==None or B==None:
            return False
            
        # L = False
        # R = False
        
        # if A.left and B.left:
        L = self.check(A.left, B.left)
        
        # if A.right and B.right:
        R = self.check(A.right, B.right)
	    
        # if A and B:
        return A.val == B.val and L and R
        # else:
        #     return False
	   
	def isSameTree(self, A, B):
	    if A == None and B == None:
	        return 1
	        
        if self.check(A,B) == True:
            return 1
        else:
            return 0