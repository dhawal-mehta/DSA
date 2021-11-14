"""
Least Common Ancestor


Problem Description

Find the lowest common ancestor in an unordered binary tree A given two values B and C in the tree.

Lowest common ancestor : the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.



Problem Constraints

1 <= size of tree <= 100000

1 <= B, C <= 109



Input Format

First argument is head of tree A.

Second argument is integer B.

Third argument is integer C.



Output Format

Return the LCA.


Example Input

Input 1:

 
      1
     /  \
    2    3
B = 2
C = 3

Input 2:

      1
     /  \
    2    3
   / \
  4   5
B = 4
C = 5



Example Output

Output 1:

 1

Output 2:

 2



Example Explanation

Explanation 1:

 LCA is 1.

Explanation 2:

 LCA is 2.
"""
"""
Hint 1
Bruteforce approach :

Pick every node. For every node, search for val1, val2 in the subtree. If val1 and val2 are both found in the subtree, then the current node is definitely one of the ancestors. Also track the depth of the current node. Pick the qualifying node of highest depth.

Hint for a better solution :

1) If you had the path from the nodes to the root, what property would the path have ? Can the paths be used to determine LCA ?
2) If you took bottom up approach using recursion, can you think of a simple solution ?
"""
"""
Solution Approach
Linear solution using path calculation :

1) Find path from root to n1 and store it in a vector or array.
2) Find path from root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch

Linear solution using recursion :

We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its parent. The parent would then test its left and right subtree if each contain one of the two nodes. If yes, then the parent must be the LCA and we pass its parent up to the root. If not, we pass the lower node which contains either one of the two nodes (if the left or right subtree contains either p or q), or NULL (if both the left and right subtree does not contain either p or q) up.
"""
# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	
    #
    # To give least common ansestor
    #
	def la(self, root, B, C):
    
        if root:
            if root.val == B or root.val == C:
                return root.val
        
            left = self.la(root.left,B,C)
            right = self.la(root.right,B,C)
            
            
            if left == -1 and right ==-1:
                return -1
            
            elif left == -1:
                return right
            elif right == -1:
                return left
            else:
                return root.val 
        else:
            return -1
    
    #
    # To check if  the element exists
    #
    def h(self,root,e):
        
        if root:
            visited = [root]
            while visited:
                node = visited.pop(0)
    
                if node.val == e:
                    return True
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
        
        return False
        
    def check(self,root,B,C):
        return self.h(root,B) and self.h(root,C)
        
    def lca(self,A,B,C):
        
        flag = self.check(A,B,C)
        
        if flag:
            return self.la(A,B,C)
        else:
            return -1
