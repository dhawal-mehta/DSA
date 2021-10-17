"""Find a peak element


Problem Description

Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.

For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 109



Input Format

The only argument given is the integer array A.


Output Format

Return the peak element.


Example Input

Input 1:

A = [1, 2, 3, 4, 5]

Input 2:

A = [5, 17, 100, 11]



Example Output

Output 1:

 5

Output 2:

 100



Example Explanation

Explanation 1:

 5 is the peak.

Explanation 2:

 100 is the peak.
"""
"""
Hint 1
Observation: Given the condition that there is only a single peak element, We can observe that the array can be one of 3 types:
1) The whole array is decreasing with atmost 1 pair of equal adjacent elements.
2) The whole array is non-increasing with atmost 1 pair of equal adjacent elements.
3) The array is increasing first, then decreasing.

Note that if there are 3 or more adjacent elements equal to each other, then there can be more than 1 peak elements. Hence, no three adjacent elements in the array are pairwise equal.
Also there can be atmost 1 pair of adjacent equal elements (i, i+1), and if exist, one of these elements must be peak element.

You need to find the index of peak element.
Can you apply binary search for the index here?
"""
"""
Solution Approach

Observation: Given the condition that there is only a single peak element, We can observe that the array can be one of 3 types:
1) The whole array is decreasing with atmost 1 pair of equal adjacent elements.
2) The whole array is non-increasing with atmost 1 pair of equal adjacent elements.
3) The array is increasing first, then decreasing.

Note that if there are 3 or more adjacent elements equal to each other, then there can be more than 1 peak elements. Hence, no three adjacent elements in the array are pairwise equal.
Also there can be atmost 1 pair of adjacent equal elements (i, i + 1), and if exist, one of these elements must be peak element.

You need to find the index of peak element.

Let us apply binary search on index. Note that this is classic binary search.
ALGORITHM:
1) Initially let l = 0 and r = A.size()-1
2) Repeat steps 3-4 while l<=r
3) Set m=(l+r)/2
4) If A[m] >= A[m-1] and A[m] >= A[m+1], A[m] is the peak element. Set ans = A[m] and exit the loop
Else if A[m] > A[m-1] we know that the peak element has to be on the right side of A[m]. Hence, we set l =m+1
Else if A[m] < A[m-1] we know that the peak element has to be on the left side of A[m]. Hence, we set r=m-1.
5) Return ans
Take extra care of edge cases, where the first or last element is the peak element.
Look for its implementation. There are multiple ways to do this.
Remember that index starts from 0.
"""
# @param A : list of integers
# @return an integer
def util(A, l, r):
    m = l+(r-l)//2
    
    
    if m==0 and A[m]>A[m+1]:
        return A[m]
        
    elif m==len(A)-1 and A[m]>A[m-1]:
        return A[m]

    elif A[m]>A[m-1] and A[m]>A[m+1]:
        return A[m]
    
    else:
        if A[m-1]>A[m]:
            return util(A,l,m-1)
        else:
            return util(A,m+1,r)
    
    
def solve(self, A):
    return util(A,0,len(A)-1)

