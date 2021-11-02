"""
Count Right Triangles

Problem Description

Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

NOTE: The answer may be large so return the answer modulo (109 + 7).



Problem Constraints

1 <= N <= 105

0 <= A[i], B[i] <= 109



Input Format

The first argument given is an integer array A.
The second argument given is the integer array B.


Output Format

Return the number of unordered triplets that form a right angled triangle modulo (109 + 7).


Example Input

Input 1:

 A = [1, 1, 2]
 B = [1, 2, 1]

Input 2:

 A = [1, 1, 2, 3, 3]
 B = [1, 2, 1, 2, 1]



Example Output

Output 1:

 1

Output 2:

 6



Example Explanation

Explanation 1:

 All three points make a right angled triangle. So return 1.

Explanation 2:

 6 quadruplets which make a right angled triangle are: (1, 1), (1, 2), (2, 2)
                                                       (1, 1), (3, 1), (1, 2)
                                                       (1, 1), (3, 1), (3, 2)
                                                       (2, 1), (3, 1), (3, 2)
                                                       (1, 1), (1, 2), (3, 2)
                                                       (1, 2), (3, 1), (3, 2)
"""
"""
Hint 1

Try fixing each point as the intersection of perpendicular and base and try finding other points.
"""
"""
Solution Approach

Try fixing each point as the intersection of perpendicular and base and try finding other points.

Once it is fixed, for the other two points, one point will share the same x-coordinate and the other point will share the same 
y-coordinate with the selected point.

For points sharing same x or y coordinate we can use map to store the points.
"""
# @param A : list of integers
# @param B : list of integers
# @return an integer
def solve( A, B):
    
    count = 0
    
    xHash = {}
    for i in A:
        if i in xHash:
            xHash[i] +=1
        else:
            xHash[i] = 1
    
    yHash = {}
    for i in B:
        if i in yHash:
            yHash[i] +=1
        else:
            yHash[i] = 1
            
    
    
    for i in range(len(A)):
        horizontalPoints = yHash[ B[i] ] - 1
        verticalPoints = xHash[ A[i] ] - 1
        
        count += horizontalPoints*verticalPoints
    
    return count