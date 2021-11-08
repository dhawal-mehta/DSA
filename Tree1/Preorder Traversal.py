"""
Preorder Traversal


Problem Description

Given a binary tree, return the preorder traversal of its nodes values.

NOTE: Using recursion is not allowed.



Problem Constraints

1 <= number of nodes <= 105


Input Format

First and only argument is root node of the binary tree, A.


Output Format

Return an integer array denoting the preorder traversal of the given binary tree.


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

 [1, 2, 3]

Output 2:

 [1, 6, 2, 3]



Example Explanation

Explanation 1:

 The Preoder Traversal of the given tree is [1, 2, 3].

Explanation 2:

 The Preoder Traversal of the given tree is [1, 6, 2, 3].
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

print(root->val);
preorderprint(root->left);
preorderprint(root->right);

Instead of calling the functions, can you put the nodes on a stack and process them ?
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
	def preorderTraversal(self, A):
        stk = []
        preo = []
        cnode = A
        
        while True:
            if cnode is not None:
                preo.append(cnode.val)
                stk.append(cnode)
                cnode = cnode.left
            elif stk:
                node = stk.pop()
                cnode = node.right
            else:
                break
        return preo