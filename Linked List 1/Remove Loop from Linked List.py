"""Remove Loop from Linked List

Problem Description

Given a linked list which contains some loop.

You need to find the node, which creates a loop, and break it by making the node point to NULL.



Problem Constraints

1 <= number of nodes <= 1000


Input Format

Only argument is the head of the linked list.


Output Format

return the head of the updated linked list.


Example Input

Input 1:

 
1 -> 2
^    |
| - - 

Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -



Example Output

Output 1:

 1 -> 2 -> NULL

Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL



Example Explanation

Explanation 1:

 Chain of 1->2 is broken.

Explanation 2:

 Chain of 4->6 is broken.
"""
"""
Hint 1
You just need to find what is the point which
has 2 poiters pointing towards it.
"""
"""
Solution Approach

You just need to find what is the point which has 2 poiters pointing towards it.
Once you have found it, remove one of the pointers
and return the head of the new linked lis
"""
def removeLoop(loop_node, head):
    ptr1 = loop_node
    ptr2 = loop_node
    k = 1
    while ptr1.next != ptr2:
        ptr1 = ptr1.next
        k += 1
    ptr1 = head
    ptr2 = head
    for i in range(k):
        ptr2 = ptr2.next
    while ptr2 != ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    while ptr2.next != ptr1:
        ptr2 = ptr2.next
    ptr2.next = None
    return head


# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        slow_p = A
        fast_p = A
        ans = None
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                if slow_p.next == fast_p:
                    slow_p.next = None
                    return A
                ans = removeLoop(slow_p, A)
                return ans