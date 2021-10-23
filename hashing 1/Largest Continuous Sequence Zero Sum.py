"""
Largest Continuous Sequence Zero Sum


Problem Description

Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.


Problem Constraints

1 <= N <= 106

-107 <= A[i] <= 107


Input Format

Single argument which is an integer array A.


Output Format

Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.


Example Input

A = [1,2,-2,4,-4]



Example Output

[2,-2,4,-4]



Example Explanation

[2,-2,4,-4] is the longest sequence with total sum of zero.
"""
"""
Hint 1

Lets try to reduce the problem to a much simpler problem.
Lets say we have another array sum where

  sum[i] = Sum of all elements from A[0] to A[i]

Note that in this array, sum of elements from A[i] to A[j] = Sum[j] - Sum[i-1]

We need to find j and i such that sum of elements from A[i] to A[j] = 0
 Or Sum[j] - Sum[i-1] = 0
 Or Sum[j] = Sum[i-1]

Now, the problem reduces to finding 2 indices i and j such that sum[i] = sum[j]
How can you solve the above problem ?
"""
"""
Solution Approach

Approach:


There are two steps:
1. Create cumulative sum array where ith index in this array represents total sum from 1 to ith index element.
2. Iterate all elements of cumulative sum array and use hashing to find two elements where value at ith index == value at jth index but i != j.
3. IF element is not present in hash in fill hash table with current element.

"""
# @param A : list of integers
# @return a list of integers
def lszero( A):
    
    ansStart = -1
    ansEnd  = -1
    store = {}
    curr_sum = 0
    flag = 0
    
    for i in range(len(A)):
        curr_sum += A[i]
        if curr_sum in store or curr_sum == 0:
            flag = 1
            if curr_sum == 0:
                ansStart = -1
                ansEnd = i
            else:
                temp = i - store[curr_sum]
                if temp > (ansEnd - ansStart):
                    ansStart = store[curr_sum]
                    ansEnd = i
        else:
            store[curr_sum] = i
    
    return A[ansStart+1:ansEnd+1]