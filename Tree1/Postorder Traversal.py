"""Postorder Traversal

Problem Description

Given a binary tree, return the Postorder traversal of its nodes values.

NOTE: Using recursion is not allowed.



Problem Constraints

1 <= number of nodes <= 105


Input Format

First and only argument is root node of the binary tree, A.


Output Format

Return an integer array denoting the Postorder traversal of the given binary tree.


Example Input

Input 1:

   1
    \
     2
    /
   3

Input 2:

   1
  / \
 6   2
    /
   3



Example Output

Output 1:

 [3, 2, 1]

Output 2:

 [6, 3, 2, 1]



Example Explanation

Explanation 1:

 The Preoder Traversal of the given tree is [3, 2, 1].

Explanation 2:

 The Preoder Traversal of the given tree is [6, 3, 2, 1]."""

"""
Hint 1
You can do this problem easily but as stated in problem recursion is not allowed here.
Stack can help you to avoid recursion. How?
"""
"""
Solution Approach
Think stack.

Recursive call would look something like this :

postorderprint(root->left);
postorderprint(root->right);
print(root->val);

Instead of calling the functions, can you put the nodes on a stack and process them ?
Would the solution be easier if you were to print the reverse of the asked ?
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
# 	def postOrderUtil(self,root):
# 	    if root
	    
	def postorderTraversal(self, A):
	    
	    ans = []
	    visited = []
	    cnode = A
	    
	    while True:
	        if cnode is not None:
	            ans.append(cnode.val)
	            visited.append(cnode)
	            cnode = cnode.right

	        elif visited:
	            node = visited.pop()
	            cnode = node.left
	        else:
	            break
        return ans[::-1]
        