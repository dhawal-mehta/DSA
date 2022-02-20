"""
Kth Smallest Element In BST


Problem Description

Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format

First and only argument is head of the binary tree A.



Output Format

Return an integer, representing the Bth element.



Example Input

Input 1:

 
            2
          /   \
         1    3
B = 2

Input 2:

 
            3
           /
          2
         /
        1
B = 1



Example Output

Output 1:

 2

Output 2:

 1



Example Explanation

Explanation 1:

2nd element is 2.

Explanation 2:

1st element is 1.
"""
"""
Hint 1

Think about the property of binary search tree and how it can help you.

Do you really need to visit right subtree of any node before visiting entire left subtree of it?
"""
"""
Solution Approach

Note the property of the binary search tree.
All elements smaller than root will be in the left subtree, and all elements greater than root will be in the right subtree.
This means we need not even explore the right subtree till we have explored everything in the left subtree. Or in other words, we go to the right subtree only when the size of left subtree + 1 ( root ) < k.

With that in mind, we can come up with an easy recursive solution which is similar to inorder traversal :

Step 1: Find the kth smallest element in left subtree decrementing k for every node visited. If answer is found, return answer.
Step 2: Decrement k by 1. If k == 0 ( this node is the kth node visited ), return node’s value
Step 3: Find the kth smallest element in right subtree.
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
	# @return an integer
	def kthsmallest(self, A, B):
        
        def util(A):
            
            curr = A
            stk = []
            while curr:
                stk.append(curr)
                curr = curr.left
            
            count =1
            while stk:
                curr = stk.pop()
                
                if count == B:
                    return curr.val
                
                count += 1
                
                curr = curr.right
                while curr:
                    stk.append(curr)
                    curr = curr.left
            
        return util(A)