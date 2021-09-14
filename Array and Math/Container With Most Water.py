"""
Container With Most Water

Problem Description

Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]).

N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.



Problem Constraints

0 <= N <= 105

1 <= A[i] <= 105



Input Format

Single Argument representing a 1-D array A.


Output Format

Return single Integer denoting the maximum area you can obtain.


Example Input

Input 1:

A = [1, 5, 4, 3]

Input 2:

A = [1]



Example Output

Output 1:

 6

Output 2:

 0



Example Explanation

Explanation 1:

 
5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6

Explanation 2:

 
No container is formed.

"""

"""
Hint 1
Area will be basically min(ai,aj)*(j-i) where j>i.

Approach 1 (in direction of O(n)) :
Will the area be maximum if you take j-i to be maximum. If not, then can you reduce the problem to simpler set?

Approach 2 (in direction of O(nlogn)) :
Sort the elements with their indexes in descending order. Start iterating from first position of sorted array while maintaing the maximum of answer. How?

"""
"""
Solution Approach

Description of approach 1:

    Note 1: When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
    Note 2: The base (N-1) is the maximum possible.

This implies that if there was a better solution possible, it will definitely have height greater than min(a1, aN).

B * H > (N-1) * min(a1, aN)
We know that, B < (N-1)
So, H > min(a1, aN)

This means that we can discard min(a1, aN) from our set and look to solve this problem again from the start.
If a1 < aN, then the problem reduces to solving the same thing for a2, aN.
Else, it reduces to solving the same thing for a1, aN-1

"""

# @param A : list of integers
# @return an integer
def maxArea(self, A):
    
    maxarea = 0
    i=0
    j=len(A)-1
    while i != j:
        area = (j-i)*min(A[i], A[j])
        if area > maxarea :
            maxarea = area
        
        if A[j]<A[i]:
            j -=1
        else:
            i+= 1
    
    return maxarea

