"""Swap List Nodes in pairs


Problem Description

Given a linked list A, swap every two adjacent nodes and return its head.

NOTE: Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.



Problem Constraints

1 <= |A| <= 106


Input Format

The first and the only argument of input contains a pointer to the head of the given linked list.


Output Format

Return a pointer to the head of the modified linked list.


Example Input

Input 1:

 A = 1 -> 2 -> 3 -> 4

Input 2:

 A = 7 -> 2 -> 1



Example Output

Output 1:

 2 -> 1 -> 4 -> 3

Output 2:

 2 -> 7 -> 1



Example Explanation

Explanation 1:

 In the first example (1, 2) and (3, 4) are the adjacent nodes. Swapping them will result in 2 -> 1 -> 4 -> 3

Explanation 2:

 In the second example, 3rd element i.e. 1 does not have an adjacent node, so it won't be swapped. """
"""
Hint 1

A->B->C.

Take a look at A,B. How can you change the next pointer of these elements without changing their values such that they are swapped?
"""
"""
Solution Approach

Lets first look at the problem of swapping 2 nodes.

Method 1: Just swap the values in the 2 nodes. In most cases, this won’t be a permissible solution.
Method 2: Move around the pointers.
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = Non
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
	    if A == None or A.next == None:
	        return A
	        
	    head = None
	    ptr3 = None
	    ptr2 = A  
	    ptr1 = A.next
	    
	    head = ptr1
	    ptr3 = ptr2
	    temp = ptr1.next
	    
	    ptr1.next = ptr2
	    ptr2.next = temp
	    
	    ptr2 = temp
	    ptr1 = ptr2.next if ptr2 and ptr2.next else None
        
        # while ptr1 != None:
        #     if head== None:
        #         head= pte
        # print(ptr1)
        # print(ptr2.val)
        # print(ptr3.val)
        while ptr1 != None:
            temp = ptr1.next
            
            #swapping
            ptr3.next = ptr1  
            ptr1.next = ptr2
            ptr2.next = temp    
            
            #next values
            ptr3 = ptr2
            ptr2 = ptr2.next   #or temp
            ptr1 = ptr2.next if ptr2 and ptr2.next else None
            
        return head