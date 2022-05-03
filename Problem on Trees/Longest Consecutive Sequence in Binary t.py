"""Longest Consecutive Sequence in Binary tree


Given a binary tree. Find the length of the longest path which comprises of nodes with consecutive values in increasing order. Every node is considered as a path of length 1.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.

Note: The longest consecutive path need to be from parent to child (cannot be the reverse).

For Example

Input 1:
                2
               /  \
              3    1
             / \ 
            4  5
Output 1:
    3
    Explanation 1:
        Longest consecutive path is 2 - 3 - 4.

Input 2:
                2
                \
                 3
                / 
               2
              /
              1     
Output 2:
     2
     Explanation 2:
        Longest consecutive path is 2  - 3. 
"""
"""
Solution Approach

Traverse the tree in top down manner.
Keep an update on the parent node value and current length sequence till this node.
If parent node value is equal to cur node value - 1 then increment current length sequence and travese further
else update current length sequence to 1 and update further.
Maximum values of current length sequecne while traversing the tree is the length of longest consecutive sequence.
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    MAX = 1
    def solve(self, A):
        if A==None:
            return 0
        
          
        self.MAX = 1
        
        def consecutive(root, currMax ):
            
            
            if root == None:
                return
            
            # print(root.val, currMax, self.MAX)
            
            if root.left:
                if root.val+1 == root.left.val:
                    self.MAX = max(self.MAX, currMax +1)
                    consecutive(root.left, currMax+1)
                else:
                    consecutive(root.left, 1)
                    
            if root.right:
                if root.val + 1 == root.right.val:
                    self.MAX = max(self.MAX, currMax+1)
                    consecutive(root.right, currMax+1)
                else:
                    
                    consecutive(root.right, 1)


        consecutive(A, 1)
        return self.MAX