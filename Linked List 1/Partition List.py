"""Partition List


Problem Description

Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B.

You should preserve the original relative order of the nodes in each of the two partitions.



Problem Constraints

1 <= |A| <= 106

1 <= A[i], B <= 109



Input Format

The first argument of input contains a pointer to the head to the given linked list.

The second argument of input contains an integer, B.



Output Format

Return a pointer to the head of the modified linked list.


Example Input

Input 1:

A = [1, 4, 3, 2, 5, 2]
B = 3

Input 2:

A = [1, 2, 3, 1, 3]
B = 2



Example Output

Output 1:

[1, 2, 2, 4, 3, 5]

Output 2:

[1, 1, 2, 3, 3]



Example Explanation

Explanation 1:

 [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.

Explanation 2:

 [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.
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
	def partition(self, A, B):
        if A == None:
            return A
            
        less = None
        prev = None
        fwd = A
        ansHead = A
        
        while fwd != None:
            # print( fwd.val )
            if fwd.val < B:
                # insert at less
                if less == None:
                    ansHead = fwd
                    less = fwd
                    
                    if prev == None:
                        prev = fwd
                    else:
                        prev.next = fwd.next
                        less.next = A
                        
                        
                    fwd = prev.next
                    # print("-----------------------")
                    # print("fwd: {}".format(fwd.val))
                    # print("prev: {}".format(prev.val))
                    # print("less: {}".format(less.val))
                    # print("ansHead: {}".format(ansHead.val))
                else:
                    if prev == less:
                        prev = prev.next
                        fwd = fwd.next
                        less = less.next
                    else:  
                        temp = fwd
                        
                        prev.next = fwd.next
                        fwd = fwd.next
                        
                        temp.next = less.next
                        less.next = temp
                        
                        less = less.next
                        
                    # print("+++++++++++++++++++")
                    # print("fwd: {}".format(fwd.val))
                    # print("prev: {}".format(prev.val))
                    # print("less: {}".format(less.val))
                    # print("ansHead: {}".format(ansHead.val))
                    # # return ansHead
                    
            else:
                if prev == None:
                    prev = fwd
                else:
                    prev = prev.next
                
                fwd = fwd.next
            
        return ansHead