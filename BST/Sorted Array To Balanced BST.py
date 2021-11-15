"""
Sorted Array To Balanced BST

Problem Description

Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints

1 <= length of array <= 100000


Input Format

First argument is an integer array A.


Output Format

Return a root node of the Binary Search Tree.


Example Input

Input 1:

 A : [1, 2, 3]

Input 2:

 A : [1, 2, 3, 5, 10]



Example Output

Output 1:

      2
    /   \
   1     3

Output 2:

      3
    /   \
   2     5
  /       \
 1         10



Example Explanation

Explanation 1:

 You need to return the root node of the Binary Tree.
"""
"""
Hint 1

What will happen when you choose middle element of array as root?

Can you simulate the same thing for the left and right part of the array after that?
"""
"""
Solution Approach

For a BST, all values lower than the root go in the left part of root, and all values higher go in the right part of the root.
For the tree to be balanced, we will need to make sure we distribute the elements almost equally in left and right part.
So we choose the mid part of the array as root and divide the elements around it .

Things to take care of :
1) Are you passing a copy of the array around or are you only passing around a reference ?
2) Are you dividing the array before passing onto the next function call or are you just specifying the start and end index ?

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        
        if A:
            h=len(A)//2
            root = TreeNode(A[h])
            if h>0:
                root.left = self.sortedArrayToBST(A[:h])
            if h<len(A):
                root.right = self.sortedArrayToBST(A[h+1:])
            return root
        else:
            return None
