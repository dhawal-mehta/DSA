"""
N max pair combinations

Problem Description

Given two integers arrays A and B of size N each.

Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.



Problem Constraints

1 <= N <= 2 * 105

-1000 <= A[i], B[i] <= 1000



Input Format

First argument is an integer array A.
Second argument is an integer array B.


Output Format

Return an intger array denoting the N maximum element in descending order.


Example Input

Input 1:

 A = [1, 4, 2, 3]
 B = [2, 5, 1, 6]

Input 2:

 A = [2, 4, 1, 1]
 B = [-2, -3, 2, 4]



Example Output

Output 1:

 [10, 9, 9, 8]

Output 2:

 [8, 6, 6, 5]



Example Explanation

Explanation 1:

 4 maximum elements are 10(6+4), 9(6+3), 9(5+4), 8(6+2).

Explanation 2:

 4 maximum elements are 8(4+4), 6(4+2), 6(4+2), 5(4+1).
"""
"""
Hint 1
Brute force is to find all combinations pair sum O(N ^ 2) and return top N max elements.
Can Sorting Work better?
"""
"""
Solution Approach

Sort both the arrays in ascending order.
Let us take priority queue (heap).
First max element is going to be the sum of the last two elements of array A and B i.e. (A[n-1] + B[n-1]).
Insert that in heap with indices of both array i.e (n-1, n-1).
Start popping from heap (n-iterations).
And insert the sum (A[L-1]+A[R]) and (A[L]+B[R-1]).
Take care that repeating indices should not be there in the heap (use map for that).
"""

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return a list of integers
	def solve(self, A, B):
        A = sorted(A)
        B = sorted(B)
        
        ptr1 = len(A)-1
        ptr2 = len(A)-1
        
        
        heap = []
        heap.append([ ptr1,ptr2,A[ptr1]+B[ptr2] ])
        count = 0
        ans = []
        dupSet = set((ptr1,ptr2))
        
        def heapifyUp(heap, root):
            if root == 1:
                return
            if heap[root-1][2] > heap[root//2 -1][2]:
                heap[root-1], heap[root//2 - 1] = heap[root//2 -1], heap[root-1]
                heapifyUp(heap, root//2)
        
        def heapifyDown(heap, root):
            if 2*root > len(heap):
                return
            
            left = 2*root
            right = 2*root + 1 if not (2*root +1 > len(heap)) else None
            
            if right != None:
                pos = left if heap[left-1][2] > heap[right-1][2] else right
                if heap[pos-1][2] > heap[root-1][2]:
                    heap[root-1], heap[pos-1] = heap[pos-1], heap[root-1]
                    heapifyDown(heap, pos)
                
            else:
                if heap[left-1][2] > heap[root-1][2]:
                    heap[root-1], heap[left-1] = heap[left-1], heap[root-1]
                
                
        
        while len(ans) < len(A):

            
            heap[0], heap[-1]= heap[-1], heap[0]
            ptr1,ptr2,currSum = heap.pop()
            
            if len(heap) > 1:
                heapifyDown(heap, 1)
            
            ans.append(currSum)
            
            if (ptr1-1, ptr2) not in dupSet:
                heap.append( [ptr1-1, ptr2, A[ptr1-1]+B[ptr2]] )
                dupSet.add( (ptr1-1,ptr2) )
                heapifyUp( heap, len(heap) )
                
            if (ptr1, ptr2-1) not in dupSet:
                heap.append( [ptr1, ptr2-1, A[ptr1]+B[ptr2-1]] )
                dupSet.add( (ptr1,ptr2-1) )
                heapifyUp( heap, len(heap) )
            
            
            
                
        return ans