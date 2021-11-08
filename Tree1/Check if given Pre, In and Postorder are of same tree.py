"""
Check if given Preorder, Inorder and Postorder traversals are of same tree


Given 3 array of integers A, B and C.

A represents preorder traversal of a binary tree.

B represents inorder traversal of a binary tree.

C represents postorder traversal of a binary tree.

Check whether these tree traversals are of the same tree or not. If they are of same tree return 1 else return 0.


Input Format

The arguments given are integer arrays A, B, and C.

Output Format

Return 1 if they are of same tree else return 0.

Constraints

1 <= length of the array <= 1000
all arrays are of same length
1 <= A[i], B[i], C[i] <= 10^9 

For Example

Input 1:
    A = [1, 2, 4, 5, 3]
    B = [4, 2, 5, 1, 3]
    C = [4, 5, 2, 3, 1]
Output 1:
    1

Input 2:
    A = [1, 5, 4, 2, 3]
    B = [4, 2, 5, 1, 3]
    C = [4, 1, 2, 3, 5]

Output 2:
    0
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    class TreeNode:
        def __init__(self,val=0):
            self.val = val
            self.left = None
            self.right = None
                
    def buildTree(self, A, B):
        
        if len(A) != len(B) or A is None or B is None:
            return None
        
        root_ele = B[-1]
        
        #Root Element
        root = TreeNode(root_ele)
        try:
            root_index_in = A.index(root_ele)
        except:
            return None
            
        
        #left subtree
        if root_index_in > -1:
            left_tree_in = A[:root_index_in] #A for left subTree
            left_tree_size = len(left_tree_in)
            left_tree_po = B[:left_tree_size] #B for left subTree
            if left_tree_in:
                left_sub_tree = self.buildTree(left_tree_in,left_tree_po)
                root.left = left_sub_tree
        
        #right subtree
        if root_index_in < len(A)-1:
            right_tree_in = A[root_index_in+1:] #A for left subTree
            right_tree_size = len(right_tree_in)
            po_s_in = len(B) - right_tree_size -1 
            right_tree_po = B[po_s_in:-1] #B for left subTree
            if right_tree_in:
                right_sub_tree = self.buildTree(right_tree_in,right_tree_po)
                root.right = right_sub_tree
        
        return root
    def solve(self, C,A, B):
        
        if len(A) != len(B) and len(B) != len(C):
            return 0
            
        #make tree from two orders
        
        root = self.buildTree(A,B)
        
        #preorder
        ans = []
        visited = []
        cnode = root
        while True:
            
            if cnode is not None:
                ans.append(cnode.val)
                visited.append(cnode)
                cnode = cnode.left
            elif visited:
                node = visited.pop()
                cnode = node.right
            else:
                break
        if ans == A:
            return 1
        else:
            return 0