"""
Count of smaller numbers after self

Problem Description

Given an array of integers A, find and return new integer array B.

Array B has the property where B[i] is the number of smaller elements to the right of A[i].



Problem Constraints

1 <= length of the array <= 100000

1 <= A[i] <= 109


Input Format

The only argument given is the integer array A.


Output Format

Return the new integer array B.


Example Input

A = [1, 5, 4, 2, 1]



Example Output

[0, 3, 2, 1, 0]



Example Explanation

Number of smaller elements to the right of 1 are 0.
Number of smaller elements to the right of 5 are 3 (4, 2, 1).
Number of smaller elements to the right of 4 are 2 (2, 1).
Number of smaller elements to the right of 2 are 1 (1).
Number of smaller elements to the right of 1 are 0.
"""
"""
Hint1

We can do this by using two loops and find the answer for each index in the array.
Time complexity for this will be O(N2). This will fail for large test case.

Can you optimize it using the merge sort algorithm?
"""
"""
Solution Approach

We can do this by using two loops and find the answer for each index in the array.
Time complexity for this will be O(N2). This will fail for large test case.

Approach 1

Use the idea of the merge sort at the time of merging two arrays.

When higher index element is less than the lower index element, it represents that the higher index element is smaller than all the elements after that lower index because the left part is already sorted.

Hence add up to all the elements after the lower index element for the required count.

Approach 2

For optimized solution we can use data compression and bit(fenwick tree).

We will sort the given data in other auxilary array and then compressed the values staring from 1.

Now for the original array, we loop through it back, first find the answer for that element using query in bit and then add the element in the bit.

Store these value in another array and return that.
"""
class Solution:
    # @param A : list of integers

    def util(self, A, pos,B,start, end):
        if start >= end:
            return
        
        mid = start + (end-start)//2
        self.util(A,pos,B,start,mid)
        self.util(A,pos,B,mid+1, end)
        
        ptr1 = start
        ptr2 = mid+1
        temp= []
        
        while ptr1 <= mid and ptr2 <= end:
            if A[pos[ptr1]] <= A[pos[ptr2]]:
                temp.append(pos[ptr2])
                ptr2+=1
            else:
                B[pos[ptr1]] += end-ptr2+1
                temp.append(pos[ptr1])
                ptr1+=1
        
        while ptr1<=mid:
            temp.append(pos[ptr1])
            ptr1+=1
        
        while ptr2 <= end:
            temp.append(pos[ptr2])
            ptr2+=1
        
        pos[start:end+1] = temp
        # print([A[i] for i in pos[start:end] ])
        
        
    def solve(self, A):
        pos = [i for i in range(0,len(A))]
        B = [0]*len(A)
        self.util(A ,pos ,B ,0 ,len(A)-1)
        # print(B)
        # print([A[i] for i in pos])
        
        return B
