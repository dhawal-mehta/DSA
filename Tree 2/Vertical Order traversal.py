"""
Vertical Order traversal

Problem Description

Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.

NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.



Problem Constraints

0 <= number of nodes <= 105


Input Format

First and only arument is a pointer to the root node of binary tree, A.


Output Format

Return a 2D array denoting the vertical order traversal of tree as shown.


Example Input

Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9

Input 2:

      1
    /   \
   3     7
  /       \
 2         9



Example Output

Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]

Output 2:

 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]



Example Explanation

Explanation 1:

 First row represent the verical line 1 and so on.
 """
 """
 Hint 1
 The idea is to traverse the tree once and get the minimum and maximum horizontal distance with respect to root. For the tree shown above, minimum distance is -2 (for node with value 2) and maximum distance is 2 (For node with value 9).
Once we have maximum and minimum distances from root, we iterate for each vertical line at distance minimum to maximum from root, and for each vertical line traverse the tree and print the nodes which lie on that vertical line.

Time Complexity: Time complexity of above algorithm is O(w*n) where w is width of Binary Tree and n is number of nodes in Binary Tree. In worst case, the value of w can be O(n) (consider a complete tree for example) and time complexity can become O(n^2).

This problem can be solved more efficiently
"""
"""
Solution Approach
We have discussed a O(n^2) solution in the previous hint. An efficient solution based on hash map is discussed.

We need to check the Horizontal Distances from root for all nodes. If two nodes have the same Horizontal Distance (HD), then they are on same vertical line. The idea of HD is simple. HD for root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal distance and a left edge is considered as -1 horizontal distance. For example, in the above tree, HD for Node 2 is at -2, HD for Node 3 is -1, HD for 5 is 0, HD for node 7 is +1 and for node 9 is +2.

We can do level order traversal of the given Binary Tree.
While traversing the tree, we can maintain HDs.
We initially pass the horizontal distance as 0 for root.
For left subtree, we pass the Horizontal Distance as Horizontal distance of root minus 1.
For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1.

For every HD value, we maintain a list of nodes in a hasp map. Whenever we see a node in traversal, we go to the hash map entry and add the node to the hash map using HD as a key in map.

Time Complexity of hashing based solution can be considered as O(n) under the assumption that we have good hashing function that allows insertion and retrieval operations in O(1) time.
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


	def verticalOrderTraversal(self, A):
	    
	    result = []
	    
	    if A:
    	    ans = defaultdict(list)
    	    visited = [(A,0)]
    	    while visited:
    	        
    	        item,h = visited.pop(0)
    	        ans[h].append(item.val)
    	        
    	        if item.left:
    	            visited.append((item.left,h-1))
    	        if item.right:
    	            visited.append((item.right,h+1))
    	    for i in sorted(ans.keys()):
    	        result.append(ans[i])
	    return result