"""
Palindrome List

Problem Description

Given a singly linked list A, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.


Problem Constraints

1 <= |A| <= 105


Input Format

The first and the only argument of input contains a pointer to the head of the given linked list.


Output Format

Return 0, if the linked list is not a palindrome.

Return 1, if the linked list is a palindrome.



Example Input

Input 1:

A = [1, 2, 2, 1]

Input 2:

A = [1, 3, 2]



Example Output

Output 1:

 1 

Output 2:

 0 



Example Explanation

Explanation 1:

 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.

Explanation 2:

 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
"""
"""
Hint 1
We need to check if first half is equal to last half(when reversed). But you can not store different copy of reversed last half as this solution will not have constant space.

Can you modify the original list to do the above task?

"""
"""
Solution Approach

To check palindrome, we just have to reverse latter half of linked list and then we can in (n/2) steps total can compare if all elements are same or not.
For finding mid point, first we can in O(N) traverse whole list and calculate total number of elements.
Reversing is again O(N).
"""
def lPalin(self, A):
    slow = A
    fast = A
    count = 1
    while fast.next != None:
        slow = slow.next
        count+= 1
        fast = fast.next
        if fast.next != None:
            fast = fast.next
            count += 1
    
    def reverse(head):
        ptr1 = head
        ptr2 = head.next
        
        while ptr2 != None:
            ptr1.next = ptr2.next
            ptr2.next = head
            head = ptr2
            
            ptr2 = ptr1.next
        
        return head

    
    if count == 1:
        return 1
        
    elif count%2 == 0:
        ptr2 = reverse(slow)
    else:
        ptr2 = reverse(slow.next)
    
    ptr1 = A
    # print(ptr2.val)
    
    for i in range(count//2):
        if ptr1.val != ptr2.val:
            return 0
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return 1