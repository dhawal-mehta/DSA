"""
Inorder Traversal

Problem Description

Given a binary tree, return the inorder traversal of its nodes values.

NOTE: Using recursion is not allowed.



Problem Constraints

1 <= number of nodes <= 105


Input Format

First and only argument is root node of the binary tree, A.


Output Format

Return an integer array denoting the inorder traversal of the given binary tree.


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

 [1, 3, 2]

Output 2:

 [6, 1, 3, 2]



Example Explanation

Explanation 1:

 The Inorder Traversal of the given tree is [1, 3, 2].

Explanation 2:

 The Inorder Traversal of the given tree is [6, 1, 3, 2].
"""
"""
Hint 1
You can do this problem easily but as stated in problem recursion is not allowed here.

Stack can help you to avoid recursion. How?
"""
"""
Solution Approach
Think stack.

Recursive call would look something like this :

inorderprint(root->left);
print(root->val);
inorderprint(root->right);

Instead of calling the functions, can you put the nodes on a stack and process them ?

How would your solution work if you were allowed to change the original tree ?
How would it work if you were not allowed to change the tree but use additional memory ( track the number of times a node has appeared in the tree ) ?
How would it work if you were not even allowed the extra memory ?
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
	def inorderTraversal(self, A):
	    ans = []
	    cnode = A
	    visited = []
	    while True:
	        if cnode is not None:
	            visited.append(cnode)
	            cnode = cnode.left
	        elif visited:
	            node = visited.pop()

	            ans.append(node.val)
	            cnode = node.right
	        else:
	            break
	       
        return ans
