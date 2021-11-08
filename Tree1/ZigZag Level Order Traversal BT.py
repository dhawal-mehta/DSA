"""
ZigZag Level Order Traversal BT


Problem Description

Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).



Problem Constraints

1 <= number of nodes <= 105


Input Format

First and only argument is root node of the binary tree, A.


Output Format

Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.


Example Input

Input 1:

    3
   / \
  9  20
    /  \
   15   7

Input 2:

   1
  / \
 6   2
    /
   3



Example Output

Output 1:

 [
   [3],
   [20, 9],
   [15, 7]
 ]

Output 2:

 [ 
   [1]
   [2, 6]
   [3]
 ]



Example Explanation

Explanation 1:

 Return the 2D array. Each row denotes the zigzag traversal of each level.
 """
 """
 Hint 1
 There are 2 approaches possible here.

1) Can you modify the level order approach to take care of this problem ? Reversing the entries in alternate row ?
2) If you don’t prefer reversing after the initial pass, can you instead use 2 stacks instead of queue to solve this problem ?
"""
"""
Solution Approach

We will be using 2 stacks to solve this problem. One for the current layer and other one for the next layer. Also keep a flag which indicates the direction of traversal on any level.

You need to pop out the elements from current layer stack and depending upon the value of flag push the childs of current element in next layer stack. You should maintain the output sequence in the process as well. Remember to swap the stacks before next iteration.

When should you terminate this algorithm?
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from collections import defaultdict 
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def zigzagLevelOrder(self, A):
	    
	    result = []
	    ans = defaultdict(list)
	    q=[(A,0)]
	    while q:
	        node,k = q.pop(0)
	        ans[k].append(node.val)
	        if node.left:
	            q.append((node.left,k+1))
	        if node.right:
	            q.append((node.right,k+1))
	            
	    
	    for i in sorted(ans.keys()):
	        result.append(ans[i][::-1] if i%2!=0 else ans[i])
	    return result