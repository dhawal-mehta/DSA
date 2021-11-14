"""
Binary tree to Circular Doubly Linked List


Problem Description

Given a binary tree convert it into circular doubly linked list based on the following rules:
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted Circular Linked List.
The order of nodes in List must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal must be the head node of the Circular List.

NOTE: You are expected to convert the binary tree into Doubly linked list in place.



Problem Constraints

1 <= Number of nodes in tree <= 100000

1 <= Value of node <= 109



Input Format

The only argument given is the root pointer of the tree, A.


Output Format

Return the head pointer of the converted circular doubly linked list.


Example Input

Input 1:

 Serialized from input of binary tree:(where 7 denotes the number of elements in serial)
    7 20 8 -1 -1 22 -1 -1 
    Binary tree is
      20 
     /  \
    8    22
    8 is the left child of 20 and 22 is the right child of 20.

Input 2:

 Serialized from input of binary tree:(where 7 denotes the number of elements in serial)
    7 10 8 -1 -1 11 -1 -1 
    Binary tree is
      10 
     /  \
    8    11
    8 is the left child of 10 and 11 is the right child of 10.



Example Output

Output 1:

     _____________
    |             |
    8 <-> 20 <-> 22
    |_____________|

Output 2:

     _____________
    |             |
    8 <-> 10 <-> 11
    |_____________|



Example Explanation

Explanation 1:

 The inorder traversal of binary tree is: [8, 20, 22]. Return the head pointer of the circular doubly linked list.

Explanation 2:

 The inorder traversal of binary tree is: [8, 10, 11]. Return the head pointer of the circular doubly linked list."""
"""
Hint 1
Think of recursively concatenating the left and right subtree of the tree into a circular double linked list.
"""
"""
Solution 1
Given the root of the tree, we will try to form the circular double linked list for each left and right subtree seperately and then concatenate each circular double linked list.

We can do this recursively, first for left subtree and then for right subtree.

Now traverse the given tree:

-> Recursively convert left subtree to a circular DLL. Let the converted list be leftlist.
-> Recursively convert right subtree to a circular DLL. Let the converted list be rightlist.
-> Make a circular linked list of root of the tree, make left and right of root to point to itself.
-> Concatenate leftlist with list of single root node.
-> Concatenate the list produced in step above with rightList.

To Concatenate two circular DLLs, we will follow below steps:

-> Get the last node of the leftlist. Retrieving the last node is an O(1) operation, since the prev pointer of the head points to the last node of the list.
-> Connect it with the first node of the right list
-> Get the last node of the second list
-> Connect it with the head of the list.
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

############################ my soltion did not woked don't know why ###################3
# class Solution:
#     # @param A : root node of tree
#     # @return the root node in the tree
#     def solve(self, A):
#         stk = []
#         myhead = None
#         curr = A
#         # test = 123
#         # print(curr.val )# curr.left.val, curr.right.val)

#         prev = None

#         while True:
#             if curr:
#                 stk.append(curr)
#                 curr = curr.left
#             elif stk:
#                 N = stk.pop()
#                 # print("here")
#                 # print("p", N.val, stk)
#                 if myhead == None:
#                     # print("herefdtfh")
#                     myhead = N
#                     # print("val", myhead.val)
#                     test = 143
#                 else:
#                     prev.right = N
#                     N.left = prev
                
#                 prev = N
#                 curr = N.right
#             else:
#                 break

#         # print(test)
#         # print(myhead.val)
#         myhead.left = prev
#         prev.right = myhead

#         return myhead


import sys 
sys.setrecursionlimit(10**5)


#
#  concatenates two doublly linked list 
#

def concatenate(leftList, rightList):
    if (leftList == None):
        return rightList
    if (rightList == None):
        return leftList

    leftLast = leftList.left

    rightLast = rightList.left
    
    if(leftLast != None):
        leftLast.right = rightList

    rightList.left = leftLast
    leftList.left = rightLast
    
    if(rightLast != None):
        rightLast.right = leftList
    return leftList

#
#  recursive function to traverse tree
#
def bTreeToCList(root):
    if (root == None):
        return None
    left = bTreeToCList(root.left)
    right = bTreeToCList(root.right)
    root.left = root
    root.right = root
    return concatenate(concatenate(left, root), right)

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        return bTreeToCList(A)
