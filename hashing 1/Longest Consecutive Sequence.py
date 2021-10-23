"""
Longest Consecutive Sequence


Problem Description

Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from the array A.


Problem Constraints

1 <= N <= 106

-106 <= A[i] <= 106


Input Format

First argument is an integer array A of size N.


Output Format

Return an integer denoting the length of the longest set of consecutive elements from the array A.


Example Input

Input 1:

A = [100, 4, 200, 1, 3, 2]

Input 2:

A = [2, 1]



Example Output

Output 1:

 4

Output 2:

 2



Example Explanation

Explanation 1:

 The set of consecutive elements will be [1, 2, 3, 4].

Explanation 2:

 The set of consecutive elements will be [1, 2].
"""
"""
Hint 1
Can we use Hashing to solve this problem?
"""
"""
Solution Approach

One solution is to sort the elements and then find longest subarray with consecutive elements. But this will take O(NlogN).

Efficient way is to use hashing.

First create an empty hash and for each element we insert, update the hash table and maxCount.

We only insert the element which are not yet inserted.
Calculate the lcount i.e the longest consecutive element till the current element - 1.
Calculate the rcount i.e the longest consecutive element from the current element + 1.

Update hMap[ele] (current element) = lcount + 1 + rcount.

Also update the maxCount.
"""
# @param A : tuple of integers
# @return an integer

def longestConsecutive(A):
    hash = set()
    
    for i in A:
        hash.add(i)
    
    max_count = 0
    total_min = 0
    total_max = 0
    
    for i in hash:
        if i-1 not in hash:
            curr = i
            count = 0
            while curr in hash:
                count += 1
                curr += 1
                
            if count > max_count:
                max_count = count
    
    return max_count