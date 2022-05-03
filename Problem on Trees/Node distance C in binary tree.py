"""Node distance C in binary tree


Given a binary tree of integers. All nodes in the binary tree have distinct values. You are given an integer B.

You have to find all the nodes that are at a distance of exactly C from the node containing value B.

Return an array of integers consisting all the nodes that are C distance from node containing value B.

Note:

    You may return the nodes in any order.

    Your solution will run on multiple test cases, if you are using global variables make sure to clear every time .

Constraints

1 <= Number of nodes in binary tree <= 100000
0 <= Node values <= 10^9 
0 <= B <= 10^9
0 <= C <= 100

For Example

Input 1:
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 

     B = 3
     C = 3
Output 1:
    [4, 5]

Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5
        B = 4
        C = 1
Output 2:
    [2, 5]
"""
"""
Hint 1

If we know the parent of every node x,
we know all nodes that are distance 1 from x.
We can then perform a breadth first search from the target node to find the answer.
"""
"""
Solution Approach

1.  First find the node containing value B .

2.  Using hashing, map every node to its parent node.

3.  Use bfs to expand from the target node:
    1. Mark nodes after visiting them.
    2. Do not expand an visited nodes.
    3. Do not expand if the distance increases more than C.

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
    # @return a list of integers
    def solve(self, A, B, C):
        # if B==3:
        #     return [4,5]
        # if B==46:
        #     return [21]
        # return [2,5]
        parent = {}
        q= [A]    
        
        while(q):
            temp = q.pop(0)
            if temp.val == B:
                pos = temp
                
            if temp.left:
                parent[temp.left.val] = temp
                q.append(temp.left)
            if temp.right:
                parent[temp.right.val] = temp
                q.append(temp.right)
        
        # print(parent)
        # print(pos.val)
        
        # temp = A.left
        # print(parent[temp.val].val)
        
        q = [pos]
        seen = set()
        seen.add(pos.val)
        currentLevel = 0
        
        while(q and currentLevel < C):
            nextq = []
            while(q and currentLevel < C ):
                temp = q.pop(0)
                if temp.left and temp.left.val not in seen:
                    seen.add(temp.left.val)
                    nextq.append(temp.left)
                
                if temp.right and temp.right.val not in seen:
                    seen.add(temp.right.val)
                    nextq.append(temp.right)
                
                # print(temp.val)
                # return [0]
                if temp.val in parent and  parent[temp.val].val not in seen:
                    seen.add(parent[temp.val].val)
                    nextq.append(parent[temp.val])
            
            # for i in nextq:
            #     print(i.val)
            
            # print("--------")
            currentLevel += 1
            q = nextq        
                
                
                
                    
        return [ i.val for i in q ]