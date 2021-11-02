"""Diffk II

Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2

Output :

1

as 3 - 1 = 2

    Return 0 / 1 for this problem.

"""
"""
Hint 1
The naive approach obviously is exloring all combinations of 2 integers using 2 loops and then check their difference.

However, lets look at it like this.
We are looking to find pair of integers where A[i] - A[j] = k, k being known entity
Lets say we fix A[i] ( i.e. we know A[i]), do we know what A[j] should be ? Once we know what A[j] we want, does it reduce to a search / lookup problem ?
"""
"""
Solution Approach
We are looking to find pair of integers where A[i] - A[j] = k, k being known entity
Lets say we fix A[i] ( i.e. we know A[i]), do we know what A[j] should be ?
A[j] = A[i] - k.

We can store all the numbers in a hashmap / hashset and then lookup A[j] in it to find out if A[j] exists.

Corner case : How do you handle case when k = 0 cleanly ?
"""

# @param A : tuple of integers
# @param B : integer
# @return an integer
def diffPossible( A, B):
    hash = set()
    flag = 0
    for i in A:
        if i in hash:
            flag = 1
        else:
            hash.add(i)

    if B != 0:
        for i in A:
            if B+i in hash or i-B in hash:
                return 1
    else:
        if flag == 1:
            return 1
    
    
    return 0
