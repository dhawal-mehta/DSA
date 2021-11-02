"""Points on same line

Problem Description

Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2D plane. A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes the y-coordinate of the ith point in 2D plane.

Find and return the maximum number of points which lie on the same line.



Problem Constraints

1 <= (length of the array A = length of array B) <= 1000

-105 <= A[i], B[i] <= 105



Input Format

First argument is an integer array A.
Second argument is an integer array B.


Output Format

Return the maximum number of points which lie on the same line.


Example Input

Input 1:

 A = [-1, 0, 1, 2, 3, 3]
 B = [1, 0, 1, 2, 3, 4]

Input 2:

 A = [3, 1, 4, 5, 7, -9, -8, 6]
 B = [4, -8, -3, -2, -1, 5, 7, -4]



Example Output

Output 1:

 4

Output 2:

 2



Example Explanation

Explanation 1:

 The maximum number of point which lie on same line are 4, those points are {0, 0}, {1, 1}, {2, 2}, {3, 3}.

Explanation 2:

 Any 2 points lie on a same line.
"""
"""
Hint 1
If two or more points lies on the same line then their slope remains same.
since slope can have double values which can cause precision problems.
Think of a solution to tackle precision problem.
"""
"""
Solution Approach



If two point are (x1, y1) and (x2, y2) then their slope will be (y2 – y1) / (x2 – x1) which can be a double value and can cause precision problems.

To get rid of the precision problems, we treat slope as pair ((y2 – y1), (x2 – x1)) instead of ratio and reduce pair by their gcd before inserting into map.

Points which are vertical or repeated are treated separately.

Note: If we use map in c++ or HashMap in Java for storing the slope pair, then total time complexity of solution will be O(n^2 logn)
"""
# @param A : list of integers
# @param B : list of integers
# @return an integer

    
def solve( A, B):
    if len(A) == 0:
        return 0

    def getSlope( x1, y1, x2, y2):
        if x2 == x1 and y2 != y1:
            return "inf"
            
        elif x2==x1 and y2 == y1:
            return "same"
        else:
            return (y2-y1)/(x2-x1)
    globalCount = 1
    for i in range( len(A) ):
        slope = {}
        localCount = 1
        for j in range( len(A) ):
            if i != j:
                tempSlope = getSlope(A[i], B[i], A[j], B[j])
                
                if tempSlope in slope:
                    slope[ tempSlope ] += 1
                    if "same" in slope:
                        localCount = max(localCount, slope[tempSlope]+slope["same"])
                        
                    localCount = max(localCount, slope[tempSlope])
                else:
                    slope[tempSlope] = 1
        # print(i)
        globalCount=max(globalCount, localCount)
    
    return globalCount + 1
                
