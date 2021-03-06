"""
The ship company

Problem Description

The local ship renting service has a special rate plan:
It is up to a passenger to choose a ship.
If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.

The passengers buy tickets in turn, the first person in the queue goes first, then goes the second one, and so on up to A-th person.

You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.



Problem Constraints

1 ≤ A ≤ 3000
1 ≤ B ≤ 1000
1 ≤ C[i] ≤ 1000
It is guaranteed that there are at least A empty seats in total.


Input Format

First argument is a integer A denoting the number of passengers in the queue.
Second arugument is a integer B deonting the number of ships.
Third argument is an integer array C of size B where C[i] denotes the number of empty seats in the i-th ship before the ticket office starts selling tickets.


Output Format

Return an array of size 2 denoting the maximum and minimum money that the ship company can earn.


Example Input

Input 1:

 A = 4
 B = 3
 C = [2, 1, 1]

Input 2:

 A = 4
 B = 3
 C = [2, 2, 2]



Example Output

Output 1:

 [5, 5]

Output 2:

[7, 6]



Example Explanation

Explantion 1:

 Maximum money can be earned if the passenger choose : 2(first ship) + 1(first ship) + 1(second ship) + 1(third ship).
 So, the cost will be 5.
 Minimum money can be earned if the passenger choose : 1(senocd ship) + 2(first ship) + 1(first ship) + 1(third ship).
 So, the cost will be 5.

Explanation 2:

 Maximum money can be earned if the passenger choose : 2(first ship) + 2(second ship) + 2(third ship) + 1(first ship).
 So, the cost will be 7.
 Minimum money can be earned if the passenger choose : 2(senocd ship) + 2(first ship) + 1(first ship) + 1(second ship).
 So, the cost will be 6."""
 """
 Hint 1

Think greedy when will the cost of tickets are maximum and minimum.

"""
"""
Solution Approach

Make 2 priority queues one for taking maximum cost tickets till now and other for the minimum.

Now for A passengers pop these 2 queues separately and take the sum of maximum and minimum answers.
"""
# @param A : integer
# @param B : integer
# @param C : list of integers
# @return a list of integers
def solve(self, A, B, C):
    
    def maxHeapDown(heap, root):
        if 2*root > len(heap):
            return
        left = 2*root
        right = None if 2*root + 1 > len(heap) else 2*root + 1
        
        if right != None:
            pos = left if heap[left-1] > heap[right-1] else right
            if heap[pos-1] > heap[root-1]:
                heap[pos-1], heap[root-1] = heap[root-1], heap[pos-1]
                maxHeapDown(heap , pos)
        else:
            if heap[left-1] > heap[root-1]:
                heap[left-1], heap[root-1] = heap[root-1], heap[left-1]
                
    
    def maxHeap(heap):
        for i in range(len(heap)//2, 0,-1):
            maxHeapDown(heap, i)
    
    def minHeapDown(heap, root):
        if 2*root > len(heap):
            return
        left = 2*root
        right = None if 2*root + 1 > len(heap) else 2*root + 1
        
        if right != None:
            pos = left if heap[left-1] < heap[right-1] else right
            if heap[pos-1] < heap[root-1]:
                heap[pos-1], heap[root-1] = heap[root-1], heap[pos-1]
                minHeapDown(heap , pos)
        else:
            if heap[left-1] < heap[root-1]:
                heap[left-1], heap[root-1] = heap[root-1], heap[left-1]
                
    
    def minHeap(heap):
        for i in range(len(heap)//2,0,-1):
            minHeapDown(heap, i)
    
    
    
    ansMax = 0
    ansMin = 0
    heap = [i for i in C]
    
    maxHeap(heap)
    
    for i in range(A):
        ansMax += heap[0]
        heap[0] -= 1
        maxHeapDown(heap, 1)
    
    heap = [i for i in C]
    minHeap(heap)
    
    for i in range(A):
        # print(heap)
        ansMin += heap[0]
        heap[0] -= 1
        
        if heap[0] == 0:
            
            heap[0],heap[-1] = heap[-1], heap[0]
            heap.pop()
        
        minHeapDown(heap, 1)        

    
    
    return [ansMax,ansMin]