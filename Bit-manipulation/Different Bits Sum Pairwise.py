"""Different Bits Sum Pairwise

Problem Description

We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2 ,..., AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.



Problem Constraints

1 <= N <= 105

1 <= A[i] <= 231 - 1



Input Format

First and only argument of input contains a single integer array A.


Output Format

Return a single integer denoting the sum.


Example Input

Input 1:

 A = [1, 3, 5]

Input 2:

 A = [2, 3]



Example Output

Ouptut 1:

 8

Output 2:

 2



Example Explanation

Explanation 1:

 f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5) 
 = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8

Explanation 2:

 f(2, 2) + f(2, 3) + f(3, 2) + f(3, 3) = 0 + 1 + 1 + 0 = 2
 """
 """
 Hint 1
 Assume that all values in input have only 1 bit i.e. Ai = 0 or 1.

How would you solve now?

Can you combine this logic if we have multiple bits?
"""
"""
Assume that all values in input have only 1 bit i.e. Ai = 0 or 1.
Lets say A = count of elements which are 0
and B = count of elements which are 1

In this case our answer is just 2 * A * B, since each such pair contributes 1 to answer.

Can you combine this logic if we have multiple bits?

Note that all bits are independent in counting, since we are counting number of bits which are different in each pair.
So, we just do the same process for all different bits. Since Ai is an integer, we just have to do this for 31 different bits, so our solution is O(31*N).
"""
# @param A : list of integers
# @return an integer
def cntBits( A):
    ans = 0
    for i in range(32):
        count1 = 0
        count0 = 0
        
        for num in A:

            if (num>>i) & 1 == 1:
                count1 += 1
            else:
                count0 += 1
                
        # print("i",i, count1, count0)
        ans = ( ans +  (count1*count0)*2 )%1000000007
    
    return ans
