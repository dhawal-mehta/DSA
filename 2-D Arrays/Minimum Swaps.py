"""Minimum Swaps

Problem Description

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.



Problem Constraints

1 <= length of the array <= 100000
-109 <= A[i], B <= 109


Input Format

The first argument given is the integer array A.
The second argument given is the integer B.


Output Format

Return the minimum number of swaps.


Example Input

Input 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8

Input 2:

 A = [5, 17, 100, 11]
 B = 20



Example Output

Output 1:

 2

Output 2:

 1



Example Explanation

Explanation 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.

Explanation 2:

 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.
 """
"""
Hint 1

Can you find the minimum number of swaps require to make all elements <= B together irrespective of the position of elements ?
"""
"""
Solution Approach

First we will find the number of elements which are less than or equal to B. Let the count comes out to be X.

We know that we need at most X-1 swaps to make all X elements to be consecutive.
Maintain a window of X and check that how many element we need to swap so that all all X elements comes in that window.

We store the minimum of all that and return that.
"""

"""
wrong approach 
# problem with this approach is that it finds out max consecutive array which is less then B , then substract it from total
# nowhere it is written that after swaps we have to maintain arrangement so there is a possiblity that in a  window (of total) there is an  element (not consecutive ) so we  will not swap it

# @param A : list of integers
# @param B : integer
# @return an integer
def solve( A, B):
    maxStart = -1
    maxEnd = -2
    start = -1
    end = -1
    total = 0
    i = 0
    while  i < len(A):
        if A[i] <= B:
            start = i
            while i<len(A) and A[i]<=B:
                total += 1
                end = i
                i+=1
            
            if end - start > maxEnd - maxStart:
                maxStart = start
                maxEnd = end
        else:
            i+=1
    print(total, maxStart, maxEnd)
    return total - (maxEnd - maxStart +1)

"""
""" accepted solution """
# @param A : list of integers
# @param B : integer
# @return an integer
def solve( A, B):
    total = 0
    for i in range(len(A)):
        if A[i] <= B:
            total += 1

    lessThenB = 0
    for i in range(total):
        if A[i] <= B:
            lessThenB += 1
    
    minSwap = total - lessThenB
    
    for i in range(total, len(A)):
        if A[i]<=B:
            lessThenB += 1
        if A[i-total] <= B:
            lessThenB -= 1
        
        if minSwap > (total-lessThenB):
            minSwap = total-lessThenB
            
    return minSwap
