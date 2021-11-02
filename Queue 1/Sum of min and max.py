"""Sum of min and max


Problem Description

Given an array A of both positive and negative integers.

Your task is to compute sum of minimum and maximum elements of all sub-array of size B.

NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.



Problem Constraints

1 <= size of array A <= 105

-109 <= A[i] <= 109

1 <= B <= size of array



Input Format

The first argument denotes the integer array A.
The second argument denotes the value B


Output Format

Return an integer that denotes the required value.


Example Input

Input 1:

 A = [2, 5, -1, 7, -3, -1, -2]
 B = 4

Input 2:

 A = [2, -1, 3]
 B = 2



Example Output

Output 1:

 18

Output 2:

 3



Example Explanation

Explanation 1:

 Subarrays of size 4 are : 
    [2, 5, -1, 7],   min + max = -1 + 7 = 6
    [5, -1, 7, -3],  min + max = -3 + 7 = 4      
    [-1, 7, -3, -1], min + max = -3 + 7 = 4
    [7, -3, -1, -2], min + max = -3 + 7 = 4   
    Sum of all min & max = 6 + 4 + 4 + 4 = 18 

Explanation 2:

 Subarrays of size 2 are : 
    [2, -1],   min + max = -1 + 2 = 1
    [-1, 3],   min + max = -1 + 3 = 2
    Sum of all min & max = 1 + 2 = 3
"""
"""
Hint 1

Can we find maximum and minimum element for each subarray in constant time?

Think of using Double ended Queue.
"""
"""
Solution Approach

We will use Deque(Double-Ended Queue) and concept of sliding window.

We create two empty double ended queues of size B (‘S’ , ‘G’) that only store indexes of elements of current window that are not useless.
An element is useless if it can not be maximum or minimum of next subarrays.
-> In deque ‘G’, we maintain decreasing order of values from front to rear.
-> In deque ‘S’, we maintain increasing order of values from front to rear.

Maintain both Dequeue such that front element gives maximum and minimum element repectively for each window.
Add that element to sum variable.
Return the sum%10^9+7.
Note that the sum%10^9+7 will be in the range (0,10^9+6).
"""
def solve(A, B):

   
   from collections import deque
   
   
   minQ = deque()
   maxQ = deque()
   sum_ = 0
   for i in range(B):
      while len(minQ) > 0 and A[minQ[-1]] >A[i]:
            minQ.pop()
      
      while len(maxQ) > 0 and A[maxQ[-1]] < A[i]:
            maxQ.pop()
      
      minQ.append(i)
      maxQ.append(i)
   
   for i in range(B, len(A)):
      sum_ = ( sum_ + A[minQ[0]] + A[maxQ[0]] )%1000000007

      
      while len(minQ)>0 and minQ[0] + B <= i:
            # print(minQ[0])
            minQ.popleft()
            
      while len(maxQ) >0 and maxQ[0] + B <= i:
            maxQ.popleft()
      
      while len(minQ) > 0 and A[minQ[-1]] >A[i]:
            minQ.pop()
      
      while len(maxQ) > 0 and A[maxQ[-1]] < A[i]:
            maxQ.pop()
      
      minQ.append(i)
      maxQ.append(i)

   
   return (sum_ + A[minQ[0]] + A[maxQ[0]] )%1000000007