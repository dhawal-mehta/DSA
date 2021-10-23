"""
Longest Subarray Sum B


Given an array of integers A of size N and an integer B.
Find the length of longest subarray having sum equal to B.

If no such subarray exists then return -1.



Input Format

The First argument given is the integer array A.
The Second argument is an integer B.

Output Format

Return the length of longest subarray having sum equal to B if exists else return -1.

Constraints

1 <= N <= 100000
-10^6 <= A[i] <= 10^6
-10^9 <= B <= 10^9

For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 10
    
Output 1:
    4

Input 2:
    A = [1, -1, -1, 1]
    B = 0
Output 2:
    4

"""
"""
Solution Approach

1. Initialize sum = 0 and maxLen = 0.
2. Create a hash table having (sum, index) tuples.
3. For i = 0 to N-1, perform the following steps:
   Accumulate A[i] to sum.
   If sum == B, update maxLen = i+1.
   Check whether sum is present in the hash table or not. If not present, then add it to the hash table as (sum, i) pair.
   Check if (sum-B) is present in the hash table or not. If present, then obtain index of (sum-B) from the hash table as index. Now check if maxLen < (i-index), then update maxLen = (i-index).
4. Return maxLen.

"""
# @param A : list of integers
# @param B : integer
# @return an integer
def solve( A, B):
    
    store = {}
    store[0] = -1
    sum_ = 0
    
    ans = -1
    for  i in range( len(A) ):
        sum_ += A[i]
        if sum_ not in store:
            store[sum_] = i
            
        if sum_ - B in store:
            ans = max(ans, i-store[sum_-B] )
    
    return ans
