"""
Aggressive cows


Problem Description

Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?



Problem Constraints

2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N


Input Format

The first argument given is the integer array A.
The second argument given is the integer B.


Output Format

Return the largest minimum distance possible among the cows.


Example Input

Input 1:

A = [1, 2, 3, 4, 5]
B = 3

Input 2:

A = [1, 2]
B = 2



Example Output

Output 1:

 2

Output 2:

 1



Example Explanation

Explanation 1:

 
John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.

Explanation 2:

 
The minimum distance will be 1.
"""
"""
Hint 1
We’ll be doing the binary search for finding the best possible maximum difference.

Since the maximum difference range between 0 to max of array.
If we sort the array then binary search starts with l=0 and r=A[n-1] and we’ve to find the maximum distance.
"""
"""
Solution Approach

We’ll be doing the binary search for finding the best possible maximum difference.

Since the maximum difference range between 0 to max of array.
If we sort the array then binary search starts with l=0 and r=A[n-1] and we’ve to find the maximum distance.
For mid in binary search, we will check whether there are B stalls such that the minimum distance is greater than equal to mid.
Finally store the maximum value we can get.

"""

def mPossible(self, A, B, m):
    end = 0
    start = 0
    count = 1
    
    while end < len(A):
        if A[end] - A[start] >= m:
            count += 1
            start = end
            if count == B:
                return 1
        
        end += 1
    return 0

    
def solve(self, A, B):
    A = sorted(A)
    # print(A)
    # l = 10**9
    l = 1

    # for i in range(len(A) - 1):
    #     if A[i + 1] - A[i] < l:
    #         l = A[i + 1] - A[i]
            
    h = A[-1] - A[0] + 1

    while(h-l > 1): #which sign should I use ??
        m = l + (h-l)//2
        if self.mPossible(A,B,m):
            if not self.mPossible(A,B,m+1):
                return m
            l = m
        else:
            h = m
            
    return l        