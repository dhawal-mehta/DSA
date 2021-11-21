"""
Magician and Chocolates


Problem Description

Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that kid can eat in A units of time.

NOTE:

    floor() function returns the largest integer less than or equal to a given number.
    Return your answer modulo 109+7



Problem Constraints

1 <= N <= 100000
0 <= B[i] <= INT_MAX
0 <= A <= 105


Input Format

First argument is an integer A.
Second argument is an integer array B of size N.


Output Format

Return an integer denoting the maximum number of chocolates that kid can eat in A units of time.


Example Input

Input 1:

 A = 3
 B = [6, 5]

Input 2:

 A = 5
 b = [2, 4, 6, 8, 10]



Example Output

Output 1:

 14

Output 2:

 33



Example Explanation

Explanation 1:

 At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates. 
 At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates. 
 At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate. 
 so, total number of chocolates eaten are 6 + 5 + 3 = 14

Explanation 2:

 Maximum number of chocolates that can be eaten is 33.
"""
"""
Hint 1

It is quite trivial to figure out that the kid will always choose the bag with the maximum number of chocolates.
By knowing this fact, how would you solve the problem ?
"""
"""
Solution Approach

The solution to this problem can be found greedily.

At any time t, the kid will always choose the bag with the maximum number of chocolates and consume all it’s chocolates.
So we need to maintain the current maximum size among all bags for every time t = 1, … , B and also updating the sizes of the bags.

This can be done using a max heap : https://en.wikipedia.org/wiki/Min-max_heap
"""
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
	    
        def maxHeapifyDown(heap, root):
            
            if 2*root > len(heap):
                return
            
            left = 2*root
            right = (2*root +1) if not(2*root +1 > len(heap)) else None
        
            if right != None:
                pos = left if heap[left-1] > heap[right-1] else right
                if heap[pos-1] > heap[root-1]:
                    heap[pos-1], heap[root-1] = heap[root-1], heap[pos-1]
                    maxHeapifyDown(heap ,pos)
            else:
                if heap[left-1] > heap[root-1]:
                    heap[left-1], heap[root-1] = heap[root-1], heap[left-1]
                    
        
        # def maxHeapifyUp(heap, root):
        #     if root ==1:
        #         return
            
        #     if heap[root//2 - 1] < heap[root-1]:
        #         heap[root//2 -1], heap[root-1] = heap[root-1], heap[root//2 -1]
        #         maxHeapifyUp(heap, root//2)
	                
        def maxHeap(heap, root):
            for i in range(root//2,0,-1):
                maxHeapifyDown(heap, i)
        
        ans = 0
        maxHeap(B, len(B))
        
        for i in range(A):
            ans = (ans + B[0])%1000000007
            B[0] = B[0]//2
            maxHeapifyDown(B, 1)
        
        return ans