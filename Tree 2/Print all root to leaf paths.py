"""
Print all root to leaf paths


You are given a binary tree. Find all paths from root to leaves of the binary tree.


Input Format

The only argument given is the root pointer of tree A.

Output Format

Return all paths from root to leaf.

Constraints

1 <= number of nodes <= 50000
0 <= A[i] <= 10^9 

For Example

Input 1:
          5
         / \
        4   8
       /   / \
      11  13  4
     /      / 
    7      5  
Output 1:
 [
   [5,4,11,7],
   [5,8,13],
   [5,8,4,5]
]    
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    

        
    def util(self,A,aux,ans):
        
        if A:
            aux1 = aux+[A.val]
            # print(aux1)
            if A.left is None and A.right is None:
                ans.append(aux1)
                return

            self.util(A.left,aux1,ans)
            self.util(A.right,aux1,ans)

        else:
            return


    def solve(self, A):
        
        aux=[]
        ans=[]
        self.util(A,aux,ans)
        return ans