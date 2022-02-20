"""
Inorder Traversal of Cartesian Tree


Given an inorder traversal of a cartesian tree, construct the tree.

    Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.

    Note: You may assume that duplicates do not exist in the tree.

Example :

Input : [1 2 3]

Return :   
          3
         /
        2
       /
      1
"""
"""
Hint 1

Given inorder traversal can you find the root here? What can you do once you get the root element and its left and right subtree?
"""
"""
Solution Approach

Inorder traversal : (Left tree) root (Right tree)

Note that the root is the max element in the whole array. Based on the info, can you figure out the position of the root in inorder traversal ? If so, can you separate out the elements which go in the left subtree and right subtree ?
Once you have the inorder traversal for left subtree, you can recursively solve for left subtree. Same for right subtree.
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @return the root node in the tree
	def buildTree(self, A):
        
        def util(i, j):
            if i>j:
                return None
                
            if i==j:
                return TreeNode(A[i])
            if j-i+1 == 2:
                if A[j] > A[i]:
                    root = TreeNode(A[j])
                    root.left = TreeNode(A[i])
                else:
                    root = TreeNode(A[i])
                    root.right = TreeNode(A[j])
                    
                return root
            
            if j-i+1 == 3:
                if A[i+1] > A[i] and A[i+1] > A[j]:
                    root = TreeNode(A[i+1])
                    root.left = TreeNode(A[i])
                    root.right = TreeNode(A[j])
                
                elif A[i] > A[i+1] and A[i]>A[j]:
                    root = TreeNode(A[i])
                    root.right = util(i+1, j)
                
                else:
                    root = TreeNode(A[j])
                    root.left = util(i,j-1)
                
                return root
            
            maxPo = -1 
            maxEle = float('-inf')
            for ind in range(i,j+1):
                if A[ind] > maxEle:
                    maxEle = A[ind]
                    maxPo = ind
            
            root = TreeNode(A[maxPo])
            
            root.left = util(i,maxPo-1)
            root.right = util(maxPo+1, j)
                
            
            return root
        
        return util(0, len(A)-1)