"""
Root to Leaf Paths With Sum

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example: Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
"""
Hint 1


Hint : Think recursion.

What if in your recursive function, you already know about the sum till the current node.

GOTCHAS :

    If you are using C++, make sure to pass the array by reference.

"""
"""
Solution Approach

Recursion might make this problem much easier to solve.

You just need to keep a track of :
1) the sum from the root to the current node.
2) The elements encountered from the root to this node.

Then it becomes a question of just checking if the current node is a leaf node, and if so, do the sum match.
If sums match, then you append the current elements from root to this node to the answer list.

Check for a node being a leaf :

  node->left == NULL && node->right == NULL

"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return a list of list of integers
	def pathSumUtil(self,A,B,li,temp_li, sum_):
        if A.left == None and A.right == None and sum_ + A.val == B:
            temp = []
            for i in temp_li:
                temp.append(i)
               
            temp.append(A.val)
            li.append(temp)
            return
       
        temp_li.append(A.val)
        if A.left:
            self.pathSumUtil(A.left,B,li,temp_li, sum_+ A.val)
        if A.right:
            self.pathSumUtil(A.right, B, li, temp_li, sum_ + A.val)
        temp_li.pop()
	    
    def pathSum(self, A, B):
        li = []
        self.pathSumUtil(A, B, li, [], 0)
        # print(li)
        
        return li
