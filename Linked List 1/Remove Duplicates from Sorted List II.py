"""Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example, Given 1->2->3->3->4->4->5, return 1->2->5. Given 1->1->1->2->3, return 2->3."""
"""
Hint 1
Maintain a pointer for distinct element encountered before current block. When to skip the current block? How can maintaining the pointer before current block can help you?

Also, take care of corner cases if any.
"""
"""
Solution Approach

Skip the node where head->next != NULL && head->val == head->next->val. Maintain a “pre” node which is the node just previous to the block of head you are checking.

Make sure you take care of corner cases :
1) Do you handle repetitions at the end ? ex : 1 -> 1
2) Do you handle cases where there is just one element ? ex : 1
3) Do you handle cases where there is just one element repeated numerous times ? 1->1->1->1->1->1
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
	   # if A is None or A.next == None:
	   #     return A
	    
	   # prev = A
    #     fwd = A.next 

    #     ansHead = None
    #     ansListPtr = None
        
    #     dupFound = 0
    #     while fwd:
    #         if fwd.val == prev.val:
    #             prev.next = fwd.next
    #             fwd = prev.next
    #             dupFound = 1
    #             continue
            
    #         if dupFound == 0:
    #             if ansHead==None:
    #                 ansHead = ListNode(prev.val)
    #                 ansListPtr = ansHead
    #             else:
    #                 ansListPtr.next = ListNode(prev.val)
    #                 ansListPtr = ansListPtr.next
                    
    #         prev = prev.next
    #         fwd = fwd.next
    #         dupFound = 0
            
    #     if dupFound == 0 and ansHead is not None:
    #         ansListPtr.next = ListNode( prev.val )
       
    #     return ansHead
    
        # if A is None or A.next == None:
        #     return A
        
        # start = A
        # end = A.next     
        
        # head = A
        # ansHead = None
        # ansPtr = None
        # flag = 0
        
        # while end != None:
            
        #     while end != None and end.val == start.val:
        #         flag = 1
        #         end = end.next
                
        #     if flag == 0:
        #         if ansHead == None:
        #             ansHead=ListNode(start.val)
        #             ansPtr=ansHead
        #         else:
        #             ansPtr.next = ListNode(start.val)
        #             ansPtr = ansPtr.next
            
        #     start = end
        #     end = end.next if end != None else None
        #     flag = 0
        
        # if flag == 0 and start != None:  # calculate if this can be shorted....
        #     if ansHead == None: 
        #         ansHead=ListNode(start.val)
        #         ansPtr=ansHead
        #     else:
        #         ansPtr.next = ListNode(start.val)
        #         ansPtr = ansPtr.next
            
        # return ansHead
        if A == None or A.next == None:
            return A
        
        ptr2 = A
        ptr1 = A.next
        
        head = None
        ptr3 = None
        
        flag = 1
        while ptr1 != None:
            flag = 1
            if ptr1.val == ptr2.val:
                flag = 0
                while ptr1 != None and ptr1.val == ptr2.val:
                    ptr1 = ptr1.next
            if flag == 0:
                
                ptr2=ptr1
                ptr1 = ptr2.next
                
            elif flag==1:
                if head ==None:
                    head = ptr2
                    ptr3 = head
                else:
                    ptr3.next = ptr2

                ptr2=ptr1
                ptr1 = ptr2.next                    
        if flag == 1:
            ptr3 = ptr2
            ptr2.next = None
        else:
            ptr3.next = None
    
        return head
