"""Another Count Rectangles


Problem Description

Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B.

(Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)



Problem Constraints

1 <= |A| <= 100000
1 <= A[i] <= 109
1 <= B <= 109



Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the number of rectangles with distinct configurations with area less than B modulo (109 + 7).


Example Input

Input 1:

 A = [1, 2]
 B = 5

Input 2:

 A = [1, 2]
 B = 1



Example Output

Output 1:

 4

Output 2:

 0



Example Explanation

Explanation 1:

 All 1X1, 2X2, 1X2 and 2X1 have area less than 5.

Explanation 2:

 No Rectangle is valid.
"""
"""
Hint 1
Consider every element as a dimension and then try
to compute what is the answer if one dimension is the selected number.
"""
"""
Solution Approach

2 pointer technique is absolutely valid here.
We would like to consider every length and breadth and calculate it.
It would look something like
while(l < a.size() && r >= 0) {
    if(1L * a[l] * a[r] < b) {
        ans = (ans + r + 1) % mod;
        l++;
    } 
    else
        r–;
    }
"""
def solve( A, B):
    p1 = 0
    p2 = len(A)-1

    ans = 0
    while  p1 <= p2:
        # print(p1,p2)
        
        if A[p1]*A[p2] < B:
            l = p2-p1 + 1
            ans = (ans + 2*l - 1)%(10**9 + 7)
            p1+=1
            
        elif A[p1]*A[p2] >= B:
            p2 -= 1

    

    return ans

