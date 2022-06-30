"""Max Sum Path in Binary Tree

Problem Description

Given a binary tree T, find the maximum path sum.

The path may start and end at any node in the tree.



Problem Constraints

1 <= Number of Nodes <= 7e4

-1000 <= Value of Node in T <= 1000



Input Format

The first and the only argument contains a pointer to the root of T, A.



Output Format

Return an integer representing the maximum sum path.



Example Input

Input 1:

  
    1
   / \
  2   3

Input 2:

       20
      /  \
   -10   20
        /  \
      -10  -50



Example Output

Output 1:

 6

Output 2:

 40



Example Explanation

Explanation 1:

     The path with maximum sum is: 2 -> 1 -> 3

Explanation 2:

     The path with maximum sum is: 20 -> 20
"""
"""
hint 1

This is a classical DP on tree problem.

Can you try to compute the answer for any vertex if you have answer for their left and right child?

"""
"""
Solution Approach

There are several ways of looking at this problem.
If we knew that root R is going to be a part of the longest path. Then we can look at the longest path to any leaf in the left subtree, longest path in the right subtree, and add them up along with root’s value to get the answer ( Obviously we only consider a path if its value is not negative ). To calculate the longest path till a leaf is O(n) [ Recursive call carrying forward the cumulative sum to a node ].
Given N possible roots, and then the O(n) leaf path calculation, the bruteforce becomes O(n^2).

However, note that the calculation of the longest path to the leaf is very redundant. So, to calculate the result for root R, can you reuse the results you have for R->left / R->right ?

"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class LRTreeNode:
    def __init__(self, L, R):
        self.val = [L, R]
        self.left = None
        self.right = None
    

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        
        global maxneg 
        # flag = False
        maxneg = float('-inf')
        
        def leftRightTree(node):
            global maxneg
            
            if node == None:
                return 0, None
            
            # print(node.val, maxneg)
            maxneg = max(maxneg, node.val)
            
            tempNode = LRTreeNode(0,0)
            
            L, tempNode.left = leftRightTree(node.left)
            R, tempNode.right = leftRightTree(node.right)
            
            
            tempNode.val = [L, R] 
            
            return max(max(tempNode.val) + node.val, 0), tempNode
        
        # def printTree(node):
        #     if node == None:
        #         return
            
        #     # print( node.val )
            
        #     printTree( node.left )
        #     print( node.val )
        #     printTree( node.right )
        
        # if maxneg < 0:
        #     return maxneg
            
        global res
        res=0
        
        def util(node, LRNode, prevMax):
            global res
            
            if prevMax  <0:
                prevMax  = 0
                
            res = max(res, LRNode.val[0]+LRNode.val[1]+node.val ,  (max(LRNode.val[0],LRNode.val[1]) + prevMax + node.val) )
            
            if node.left != None:
                util(node.left, LRNode.left, max(LRNode.val[1] , prevMax) + node.val)
            
            if node.right != None:
                util(node.right, LRNode.right, max(LRNode.val[0] , prevMax)+ node.val)

        
        _, LRHead  = leftRightTree(A)
        # printTree(LRHead)
        
        if maxneg < 0:
            return maxneg
        
        util(A, LRHead, 0)
        
        return res
        
            