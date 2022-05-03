"""
BST nodes in a range


Problem Description

Given a binary search tree of integers. You are given a range B and C.

Return the count of the number of nodes that lie in the given range.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= B < = C <= 109



Input Format

First argument is a root node of the binary tree, A.

Second argument is an integer B.

Third argument is an integer C.



Output Format

Return the count of the number of nodes that lies in the given range.



Example Input

Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 12
     C = 20

Input 2:

            8
           / \
          6  21
         / \
        1   7

     B = 2
     C = 20



Example Output

Output 1:

 5

Output 2:

 3



Example Explanation

Explanation 1:

 Nodes which are in range [12, 20] are : [12, 14, 15, 20, 16]

Explanation 2:

 Nodes which are in range [2, 20] are : [8, 6, 7]

"""
"""
Hint 1

The idea is to traverse the given binary search tree starting from the root. 

"""
"""
Solution Approach

The idea is to traverse the given binary search tree starting from the root.
For every node being visited, check if this node lies in range,
if yes, then add 1 to the result and recur for both of its children.
If the current node is smaller than the low value of the range, then recur for the right child; else recur for the left child.

"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        def trim(root, L, R):
            # 
            if root == None:
                return 0
            # print(root.val)
            if root.val < L:
                return trim(root.right, L, R)
            
            elif root.val > R:
                return trim(root.left, L, R)
            
            else:
                if root.val == L:
                    return 1 + trim(root.right, L, R)
                elif root.val ==R:
                    return 1 + trim(root.left, L, R)
                else:
                    return trim(root.left, L, R) + trim(root.right, L, R) + 1
        # print("test")
        # return 0
        return trim(A, B, C) 
            