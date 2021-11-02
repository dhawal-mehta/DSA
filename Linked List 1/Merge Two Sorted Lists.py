"""Merge Two Sorted Lists

Problem Description

Merge two sorted linked lists A and B and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.



Problem Constraints

0 <= |A|, |B| <= 105


Input Format

The first argument of input contains a pointer to the head of linked list A.

The second argument of input contains a pointer to the head of linked list B.



Output Format

Return a pointer to the head of the merged linked list.


Example Input

Input 1:

 A = 5 -> 8 -> 20
 B = 4 -> 11 -> 15

Input 2:

 A = 1 -> 2 -> 3
 B = Null



Example Output

Output 1:

 4 -> 5 -> 8 -> 11 -> 15 -> 20

Output 2:

 1 -> 2 -> 3



Example Explanation

Explanation 1:

 Merging A and B will result in 4 -> 5 -> 8 -> 11 -> 15 -> 20 

Explanation 2:

 We don't need to merge as B is empty.
  """
"""
Hint 1
Maintain pointers in both the linked list and keep appending the elements to the list to be returned.

NOTE: You don’t have to create new nodes here i.e. list to be returned should be made from the combination of both of the given lists.
"""
"""
Solution Approach
First thing to note is that all you would want to do is modify the next pointers. You don’t need to create new nodes.

At every step, you choose the minumum of the current head X on the 2 lists, and modify your answer’s next pointer to X. You move the current pointer on the said list and the current answer.

Corner case,
Make sure that at the end of the loop, when one of the list goes empty, you do include remaining elemnts from the second list into your answer.

Test case : 1->2->3 4->5->6
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
        head1 = A if A.val > B.val else B
        head2 = B if A.val > B.val else A
        ans = head2
        
        prev_head2 = None
        while head1 != None and head2 != None:
            temp = head1.next
            
            while head2 != None and head2.val <= head1.val:
                prev_head2 = head2
                head2 = head2.next
                
            if head2 != None and head2.val > head1.val:
                head1.next = head2
                prev_head2.next = head1
                prev_head2 = head1
                head1 = temp
                
        if head1 != None:
            prev_head2.next = head1
        
        return ans