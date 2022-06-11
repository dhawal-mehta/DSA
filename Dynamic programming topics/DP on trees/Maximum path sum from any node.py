"""
Maximum path sum from any node


Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

Example 1:

Input:
     10
    /  \
   2   -25
  / \  /  \
 20 1  3  4
Output: 32
Explanation: Path in the given tree goes
like 10 , 2 , 20 which gives the max
sum as 32.

Example 2:

Input:
     10
   /    \
  2      5
          \
          -2
Output: 17
Explanation: Path in the given tree goes
like 2 , 10 , 5 which gives the max sum
as 17.

Your Task:
You don't need to take input or print anything. Your task is to complete the function findMaxSum() that takes root as input and returns max sum between any two nodes in the given Binary Tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 103
1 ≤ |Data on node| ≤ 104
"""
"""
Hint 1
For each node there can be four ways that the max path goes through the node:
1. Node only
2. Max path through Left Child + Node
3. Max path through Right Child + Node
4. Max path through Left Child + Node + Max path through Right Child

The idea is to keep trace of four paths and pick up the max one in the end. An important thing to note is, root of every subtree needs to return maximum path sum such that at most one child of root is involved. This is needed for parent function call.
"""
#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def __init__(self):
        self.ans = float('-inf')
        
        
    def util(self, root):
        if root==None:
            return 0
        
        lt = self.util( root.left )
        rt = self.util( root.right )
        
        temp = max(max(lt,rt) + root.data, root.data)
        
        temp2 =  max(temp, lt+rt+root.data)
        
        self.ans = max(self.ans, temp2)
        
        return temp
        
    def findMaxSum(self, root): 
        #Your code here
        self.util(root)
        return self.ans
        

## alternate
import sys
sys.setrecursionlimit(100000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

   
