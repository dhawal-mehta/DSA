"""
Sum Root to Leaf Numbers


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12. The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
"""
"""
Hint 1

Can you traverse the tree while keeping the number%1003 from root to current node?

How can you check if you have reached the leaf or not?
"""
"""
Solution Approach

Think recursion.
Carrying along the number formed from root to the node when calling the function for node, will make stuff easier for you. When you encounter a new digit, you can append it to existing one as newNum = oldNum * 10 + newDigit.
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def sum_(self,root, sum_yet ):
	    if root.left ==None and root.right  == None:
	        return  ( sum_yet*10 + root.val ) % 1003
	   
        L = 0
        R = 0
        if root.left:
            L = self.sum_(root.left, (sum_yet*10 + root.val)%1003 )
        if root.right:
            R = self.sum_(root.right, (sum_yet*10 + root.val)%1003 )
        
        return (L+ R)%1003
        
	def sumNumbers(self, A):
        return self.sum_(A,0)