"""
Replace in List


Given heads A and B of two linked lists L1 and L2 respectively and given 2 integers C and D such that 0≤C≤D.

You have to replace L1[C,D] with L2 (including both indices C and D) and return the resultant list.

Note:

    Index starts from 0.
    D < total number of elements in L1.
    You can only use constant amount of extra memory.

Example

L1 = 1->7->3->9->2->8->1->End.

L2 = 3->1->9->8->5->End.

C=2

D=4

Resultant list L = 1->7->3->1->9->8->5->8->1->End."""

"""
Hint 1
Can you figure out the position of node from start from where you have to replace?
Can you figure out the position of node from start till where you have to replace?
"""
"""
Solution Approach

Try to solve the problem like array. The resultant array will have size of lenA+lenB-(D-C+1) and it contains elements of A till C then fully B

then the elements of A from D+1.

Simply, The solution has four parts:

1) Find the first node from where you have to replace the linked list.

2) Find the last node from till where you have to replace the linked list.

3) Attach the other linked list from first node.

4) Attach the end of other linked list to last node of the linked list.

Return the head of the first linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @param C : integer
    # @param D : integer
    # @return the head node in the linked list
    def solve(self, A, B, C, D):
        if A ==None or B == None:
            return None
            
        count = 1
        curr = A
        if C!=0:
            while count < C:
                curr = curr.next
                count += 1
    
            temp = curr.next
            curr.next = B
            
        else:
            temp = A
            count = 0
            
        end_b = B
        while end_b.next != None: 
            end_b = end_b.next
        
        while count < D:
            temp = temp.next 
            count += 1
        
        end_b.next = temp.next 
        
        return A if C != 0 else B
    