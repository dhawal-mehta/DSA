"""
Left view of binary tree


Problem Description

Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.

Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side

NOTE: The value comes first in the array which have lower level.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 109



Input Format

First and only argument is a root node of the binary tree, A.


Output Format

Return an integer array denoting the left view of the Binary tree.


Example Input

Input 1:

            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 

Input 2:

            1
           /  \
          2    3
           \
            4
             \
              5



Example Output

Output 1:

 [1, 2, 4, 8]

Output 2:

 [1, 2, 4, 5]



Example Explanation

Explanation 1:

 The Left view of the binary tree is returned."""
 """
Hint 1
Try to Modify the the level order traversal of tree to find the solution for this problem.
"""
"""
Solution Approach
For each level whenever you encounters the first node on that level append it to the answer.

Try to Modify the the level order traversal of tree for this problem.

You can use queue to solve this problem as we do in level order traversal.
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    
    def solve(self, A):
        ans = []
        if A:
            visited = [(A,0)]
            l=0
            while visited:
                item,i = visited.pop()
                if i == l:
                    ans.append(item.val)
                    l=l+1
                if item.right:
                    visited.append((item.right,i+1))
                if item.left:
                    visited.append((item.left,i+1))
        return ans