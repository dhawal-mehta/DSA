"""
Connect ropes


Problem Description

Given an array of integers A representing the length of ropes.

You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths.

Find and return the minimum cost to connect these ropes into one rope.



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 1000


Input Format

The only argument given is the integer array A.


Output Format

Return an integer denoting the minimum cost to connect these ropes into one rope.


Example Input

Input 1:

 A = [1, 2, 3, 4, 5]

Input 2:

 A = [5, 17, 100, 11]



Example Output

Output 1:

 33

Output 2:

 182



Example Explanation

Explanation 1:

 Given array A = [1, 2, 3, 4, 5].
 Connect the ropes in the following manner:
 1 + 2 = 3
 3 + 3 = 6
 4 + 5 = 9
 6 + 9 = 15

 So, total cost  to connect the ropes into one is 3 + 6 + 9 + 15 = 33.

Explanation 2:

 Given array A = [5, 17, 100, 11].
 Connect the ropes in the following manner:
 5 + 11 = 16
 16 + 17 = 33
 33 + 100 = 133

 So, total cost  to connect the ropes into one is 16 + 33 + 133 = 182.
"""
"""
Hint 1

Suppose you have 3 ropes of Length L1, L2 and L3.

First combine L1 and L2 with cost = L1 + L2, then combine L3 with rope of Length L2 + L1 with cost = L1 + L2 + L3.

TotaL cost = L1 + L2 + L1 + L2 + L3 = 2*(L1 + L2) + L3.

To minimize the totaL cost, We should combine ropes of minimum Length first to minimize the L1 + L2 factor.
"""
"""
Solution Approach

As mentioned in the hint, We should combine the ropes of minimum length first to get the minimum overall cost.
Let’s try to observe with an example: Suppose we are given 4 ropes of length 4, 6, 8 and 10.

1) First connect ropes of lengths 4 and 6. Now, we have three ropes of length 10(4 + 6), 8 and 10.
2) Now connect ropes of lengths 8 and 10. Now, we hace two ropes of length 18(8 + 10) and 10(4 + 6).
3) Now connect both the ropes with cost 18(8 + 10) + 10(4 + 6) = 28 (4 + 6 + 8 + 10).

So, total cost is 28 + 10 + 18 = 56. If we try to connect in some other way, the cost will >= 56.

Let’s try to find how many times each given initial lengths are added to the final cost.

In the first step, combine 4 and 6 and the cost of connecting them is 10 = 4 + 6.
In second step, combine 8 + 10(4 + 6) and cost of connecting them is 18 = 8 + 4 + 6.
In last step, combine 18 + 10 and cost of connecting them is 28 = 8 + 4 + 6 + 10.

So, it is easy to observe that 4 and 6 are added the most number of times, lengths of the ropes which are picked first are included more than once in total cost. So, the idea is to connect the smallest two ropes first and recur for remaining ropes.

To find the answer, take the two ropes with the smallest lengths and combine these ropes. Keep on doing this until we have only one rope left. This can easily be done using priority_queue.
"""
class Solution:
    
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        # heap = A
        
        # def heapifyDown(root):
        #     if root== None or 2*root > len(heap):
        #         return
            
        #     left = 2*root
        #     right = (2*root +1) if not (2*root + 1 > len(heap) ) else None
            
        #     if right != None:
        #         pos = left if heap[left-1] < heap[right-1] else right
        #         if heap[pos-1] < heap[root-1]:
        #             heap[root-1], heap[pos-1] = heap[pos-1], heap[root-1]
        #             heapifyDown(pos)
        #     else:
        #         if heap[left-1] < heap[root-1]:
        #             heap[root-1], heap[left-1] = heap[left-1], heap[root-1]
                
        # def heapifyUp(root):
        #     if root == 1:
        #         return

        #     if heap[root//2 -1] > heap[root-1]:
        #         heap[root//2 -1], heap[root-1] = heap[root -1], heap[root//2 -1]
        #         heapifyUp(root//2)
                
        
        # def minHeap(root):
        #     for i in range(root//2, 0,-1):
        #         heapifyDown(i)
        
        # ans = 0
        # minHeap(len(A))
        
        # print(A)
        
        # while len(A) > 1:

        #     A[0], A[-1] = A[-1], A[0]
        #     num1 = A.pop()
        #     heapifyDown(1)
            
            
        #     ans += num1 + A[0]
        #     A[0] = num1+A[0]
        #     heapifyDown(1)
        
        
        from queue import PriorityQueue
        
        # li = [3,4,6,2,5]
        # print(li)
        pq = PriorityQueue()
        [pq.put(i) for i in A ]
        # l1 = pq.get()
        # l2 = pq.get()
        # print(l1, l2)
        N = len(A) -1
        ans = 0
        while N > 0:
            l1 = pq.get()
            l2 = pq.get()
            # print(l1, l2)
            ans += l1+l2
            pq.put(l1+l2)
            N-=1
            
        # print(ans)
        return ans