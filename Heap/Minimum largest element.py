"""
Minimum largest element

Problem Description

Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add original value(value stored at index before we did any operations) to it's current value. You can choose any of the N elements in each operation.

Perform B operations in such a way that the largest element of the modified array(after B operations) is minimised. Find the minimum possible largest element after B operations.



Problem Constraints

1 <= N <= 106
0 <= B <= 105
-105 <= A[i] <= 105


Input Format

First argument is an integer array A.
Second argument is an integer B.


Output Format

Return an integer denoting the minimum possible largest element after B operations.


Example Input

Input 1:

 A = [1, 2, 3, 4] 
 B = 3

Input 2:

 A = [5, 1, 4, 2] 
 B = 5



Example Output

Output 1:

 4

Output 2:

 5



Example Explanation

Explanation 1:

 Apply operation on element at index 0, the array would change to [2, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [3, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [4, 2, 3, 4]
 Minimum possible largest element after 3 operations is 4.

Explanation 2:

 Apply operation on element at index 1, the array would change to [5, 2, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 3, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 4, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 5, 4, 2]
 Apply operation on element at index 3, the array would change to [5, 5, 4, 4]
 Minimum possible largest element after 5 operations is 5.
"""
"""
Hint1

Consider current and the next value of every element of an array. How can we pick the best possible element so that the largest element is minimized?
Will using a min heap of the next states of the elements of an array help?
"""
"""
Solution Approach

Let’s keep a state array to keep track of the value of every element in the array after K operations.
Maintain a state array, which tells about the state of the array after every operation.
Initially state array will be the same as the inital array.

We need to consider the next state of every element in the array.
Consider a min heap. And initially push the next state of every element in the heap.
Note that you need to keep track of the indices of every element in the heap, present in the initial array.
Pick the top element, and change the state of that element, in the state array. Pop this element and push the next state in the heap.
At every operation we are choosing the element who’s next state is minimum, hence there are only two possibilities:
1) Either the maximum element remains same, and we return that element directly.
2) The next state of popped element is the maximum.
We made sure changing the state of this element is the best option, as the next state of this element is the minimum.
Hence the maximum will be the least using this approach.
"""
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
	   # print(B, max(A))
	    if B==0 or B==None:
	        return max(A)
	        
        # arr = [i for i in A]
        heap = [ [A[i],2*A[i] ] for i in range(len(A)) ]
        
        
        def heapifyDown(heap, root):
            if 2*root > len(heap):
                return
            
            left = 2*root
            right = (2*root+1) if not (2*root+1) > len(heap) else None
            
            if right != None:
                pos = left if heap[left-1][1] < heap[right-1][1] else right
                if heap[pos-1][1] < heap[root-1][1]:
                    heap[pos-1], heap[root-1] = heap[root-1],heap[pos-1]
                    heapifyDown(heap, pos)
                    
            else:
                if heap[left-1][1] < heap[root-1][1]:
                    heap[left-1], heap[root-1] = heap[root-1], heap[left-1]

                
        def minHeap(heap, root):
            for i in range(root//2, 0,-1):
                heapifyDown(heap, i)
        
        minHeap(heap, len(heap))
        # print(heap)
        
        for i in range(B):        

            # pos, num = heap[0]
            # arr[pos] += A[pos]
            # num += pos
            heap[0][1] += heap[0][0]
            heapifyDown(heap, 1)

        # print(heap)
        ans = -10**9
        
        for i in heap:
            ans = max(ans, i[1] - i[0])
            
        return ans