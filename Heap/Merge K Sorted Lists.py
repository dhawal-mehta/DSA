"""
Merge K Sorted Lists


Problem Description

Given a list containing head pointers of N sorted linked lists. Merge these N given sorted linked lists and return it as one sorted list.


Problem Constraints

1 <= total number of elements in given linked lists <= 100000


Input Format

First and only argument is a list containing N head pointers.


Output Format

Return a pointer to the head of the sorted linked list after merging all the given linked lists.


Example Input

Input 1:

 1 -> 10 -> 20
 4 -> 11 -> 13
 3 -> 8 -> 9

Input 2:

 10 -> 12
 13
 5 -> 6



Example Output

Output 1:

 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

Output 2:

 5 -> 6 -> 10 -> 12 ->13



Example Explanation

Explanation 1:

 The resulting sorted Linked List formed after merging is 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20.

Explanation 2:

 The resulting sorted Linked List formed after merging is 5 -> 6 -> 10 -> 12 ->13.
"""
"""
Hint 1

Lets keep a pointer for every linked list. At any instant you will need to know the minimum of elements at all pointer. Following it you will need to advance that pointer. Can you do this in complexity better than O(K).

Preferably O(logK). But how?
"""
"""
Solution Approach

There are 2 approaches to solving the problem.

Approach 1 : Using heap.
At every instant, you need the minimum of the head of all the k linked list. Once you know the minimum, you can push the node to your answer list, and move over to the next node in that linked list.

Approach 2 : Divide and conquer.
Solve the problem for first k/2 and last k/2 list. Then you have 2 sorted lists. Then simiply merge the lists.
Analyze the time complexity.
T(N) = 2 T(N/2) + N
T(N) = O (N log N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Item:
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        return self.item.val < other.item.val
    
    def __repr__(self):
        return str(self.item.val)

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        import heapq

        heap = []
        for i in A:
            heapq.heappush(heap, Item(i))

        head = None
        prev = None

        while heap:
            node = heapq.heappop(heap).item

            if head == None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

            if node.next:
                heapq.heappush(heap, Item(node.next))
                
        
        return head