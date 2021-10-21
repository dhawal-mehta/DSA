"""
Chocolate Distribution


Problem Description

Given an array A of N integers where each value represents number of chocolates in a packet.

i-th can have A[i] number of chocolates.

There are B number students, the task is to distribute chocolate packets following below conditions:

1. Each student gets one packet.
2. The difference between the number of chocolates in packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

Return the minimum difference (that can be achieved) between maximum and minimum number of chocolates distributed.



Problem Constraints

0 <= N <= 10^5
1 <= A[i] <= 10^7
0 <= B <= 10^5



Input Format

The first argument contains an integer array A.

The second argument contains an integer B.



Output Format
Return the minimum difference (that can be achieved) between maximum and minimum number of chocolates distributed.


Example Input

Input:

  A : [3, 4, 1, 9, 56, 7, 9, 12]
  B : 5



Example Output

Output:

  6



Example Explanation

Explanation:

  Minimum Difference is 6
  The set goes like 3,4,7,9,9 and the output is 9-3 = 6
"""
"""
Hint 1
Sort the array and observe the pattern.
"""
"""
Solution Approach
Sort the array.

Find the minimum difference between all subarrays of size B
"""
# @param A : list of integers
# @param B : integer
# @return an integer
def solve( A, B):
    if B==0 or len(A)==0:
        return 0
        
    A = sorted(A)

    min_ = 10**9
    i=0
    while B + i -1 < len(A):
        temp = A[B+i-1] - A[i]
        if temp < min_:
            min_ = temp
        i+=1
    
    return min_