"""
K reverse linked list


Problem Description

Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return modified linked list.


Problem Constraints

1 <= |A| <= 103

B always divides A



Input Format

The first argument of input contains a pointer to the head of the linked list.

The second arugment of input contains the integer, B.



Output Format

Return a pointer to the head of the modified linked list.


Example Input

Input 1:

 A = [1, 2, 3, 4, 5, 6]
 B = 2

Input 2:

 A = [1, 2, 3, 4, 5, 6]
 B = 3



Example Output

Output 1:

 [2, 1, 4, 3, 6, 5]

Output 2:

 [3, 2, 1, 6, 5, 4]



Example Explanation

Explanation 1:

 For the first example, the list can be reversed in groups of 2.
    [[1, 2], [3, 4], [5, 6]]
 After reversing the K-linked list
    [[2, 1], [4, 3], [6, 5]]

Explanation 2:

 For the second example, the list can be reversed in groups of 3.
    [[1, 2, 3], [4, 5, 6]]
 After reversing the K-linked list
    [[3, 2, 1], [6, 5, 4]]
"""
"""
Hint 1
You can try to split the given linked list into bucket of K and try to solve the problem for those fixed buckets of size K.
How will you solve the problem if you have to reverse the whole linked list?

Moreover, you would try to somehow link the buckets after you have individually solved each of them, try thinking on how to achieve
linking and reversing of the buckets using minimum number of pointers.

Problems like these are using a divide and conquer type of approach where the bucket size is fixed. First you divide the given list
into |A|/K parts and then solve each one individually and then link the answers together.
"""
"""
Solution Approach

The given linked list can be split into bucket of length K. For doing this, you can use two pointers that are K elements apart in the linked
list.

Now, let us try to solve the problem for one bucket i.e. reversing
a single linked list. For this, you can check this.

So now, our problem has been modified to solving the problem for each bucket and then concatenating the lists to get a final
K-reversed linked list which is just an implementation issue.
The given linked list can be split into bucket of length K. For doing this, you can use two pointers that are K elements apart in the linked
list.

Now, let us try to solve the problem for one bucket i.e. reversing
a single linked list. For this, you can check this.

So now, our problem has been modified to solving the problem for each bucket and then concatenating the lists to get a final
K-reversed linked list which is just an implementation issue.
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def revListUtil(self,head, l):
	    back = head
	    fwd = back.next
	     
	    while l > 1:
	        temp = fwd.next
	        fwd.next = head
	        head = fwd
	        
	        back.next = temp
	        fwd = temp
	        l -= 1
	        

        
	def reverseList(self, A, B):
	    if A == None:
	        return A
	        
	    head = A
	    prev = A

	    count = 1
	    
	    for i in range(0,B-1):
	        if prev.next:
	            count += 1
	            prev = prev.next
	 
	    self.revListUtil(A,count)
        head.next = self.reverseList(head.next,B)
        
        return prev
    
            
	    
	    
	    
