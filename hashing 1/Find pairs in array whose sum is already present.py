"""
Find pairs in array whose sum is already present

Given an array A of N distinct and positive elements, the task is to find number of unordered pairs whose sum already exists in given array.

Expected Complexity : n^2

CONSTRAINTS

1 <= N <= 1000
1 <= A[i] <= 10^6 + 5

SAMPLE INPUT

A : [ 3, 4, 2, 6 ,7]

SAMPLE OUTPUT

2

EXPLANATION

The pairs following the conditions are : 
(2,4) = 6,
(3,4) = 7

"""
# @param A : list of integers
# @return an integer
def solve(A):
    hash = set()
    for i in A:
        hash.add(i)
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i]+A[j] in hash:
                # print(A[i], A[j])
                count += 1
    
    return count