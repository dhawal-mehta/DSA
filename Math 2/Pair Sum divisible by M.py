""" Pair Sum divisible by M

Problem Description

Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.

Since the answer may be large, return the answer modulo (109 + 7).



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 106


Input Format

The first argument given is the integer array A.
The second argument given is the integer B.


Output Format

Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).


Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
 B = 2

Input 2:

 A = [5, 17, 100, 11]
 B = 28



Example Output

Output 1:

 4

Output 2:

 1



Example Explanation

Explanation 1:

 All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5). 
 So total 4 pairs."""
 """
 Hint 1

 Trivial way of solving is to count the number of pair whose sum is divisble by B by using two loops over the array.

Can you think of optimizing it by using the fact that the value is upto 106 and using modulo operator we can reduce all the elements in the range 0 to B-1.
"""
"""
Solution Approach


Let’s optimize using the fact that the value is upto 106 and using modulo operator we can reduce all the elements in the range 0 to B-1.

We make an auxillary array cnt, the index i denotes the number of elements which gives i as remainder when divided by B.
Now, we know that sum of the pair modulo B should be equal to 0.
So we will count the pairs that give sum of the pair modulo B is 0.
We can do this by adding cnt[i]*cnt[j] in the answer such that (i + j)%B=0.
Note: Keep in mind the base case when i==0 and j==0 and i==j.
"""
""" Accepted solution """
def solve(A, B):
    freq = {}
    for i in A:
        mod = i%B
        if mod in freq:
            freq[mod] += 1
        else:
            freq[mod] = 1
    
    ans = 0
    if 0 in freq:
        ans = ( (freq[0]*(freq[0] - 1))//2 )%(10**9 + 7)

    for i in freq:
        if i!=0 and i <= B-i:
            if i != B-i and B-i in freq:
                ans = (ans + freq[i]*freq[B-i] )%(10**9 + 7)
            elif i == B-i:
                ans = (ans + (freq[i]*(freq[i]-1))//2 )%(10**9 + 7)

    
    
    return ans