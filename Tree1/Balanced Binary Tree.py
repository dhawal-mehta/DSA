"""
Balanced Binary Tree

Problem Description

Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints

1 <= size of tree <= 100000


Input Format

First and only argument is the root of the tree A.


Output Format

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.


Example Input

Input 1:

    1
   / \
  2   3

Input 2:

 
       1
      /
     2
    /
   3



Example Output

Output 1:

1

Output 2:

0



Example Explanation

Explanation 1:

It is a complete binary tree.

Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1. 
"""
"""
Hint 1
Think recursively.

How can you maintain the depth of subtree of every node?
"""
"""
Solution Approach
A tree is balanced if :
1) Left subtree is balanced
2) Right subtree is balanced
3) And the difference is height of left and right subtree is atmost 1.

Can you think of a way to simulate that with recursion ?
Note that depth of a tree can also be calculated recursively as max(depth(rightSubtree), depth(leftSubtree)) + 1.
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
	def isBalanced(self, A):
        def util(Node):
            if Node == None:
                return 0
            
            lh = util(Node.left)
            rh = util(Node.right)
            
            if lh<0 or rh < 0 or abs(lh-rh) > 2:
                return -1
            
            return max(lh, rh) +1
            
        return 1 if util(A) >= 0 else 0