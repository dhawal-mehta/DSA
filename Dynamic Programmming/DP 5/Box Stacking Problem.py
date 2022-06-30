"""
Box Stacking Problem


Problem Description
Given a matrix of integers A of size N x 3 representing the dimensions of N rectangular 3-D boxes, where A[i][0] represents the height of the ith box, A[i][1] represents the widht of the ith box and A[i][2] represents the length of the ith box.

You want to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. You can rotate a box so that any side functions as its base. It is also allowable to use multiple instances of the same type of box.

Find and return the maximum height of stack achievable.


Problem Constraints

1 <= N <= 1000
1 <= A[i][0], A[i][1], A[i][2] <= 1e6


Input Format

The only argument given is the integer matrix A.


Output Format

Return a single integer, the maximum height of stack achievable.


Example Input

Input 1:

A = [   [4, 6, 7]
        [1, 2, 3]
        [4, 5, 6]
        [1, 2, 3]   ]

Input 2:

A = [   [4, 5, 6]
        [10, 12, 14]    ]



Example Output

Output 1:

60

Output 2:

34



Example Explanation

Explanation 1:

Following are all rotations of the boxes in decreasing order of base area:
        10 x 12 x 32
        12 x 10 x 32
        32 x 10 x 12
        4 x 6 x 7
        4 x 5 x 6
        6 x 4 x 7
        5 x 4 x 6
        7 x 4 x 6
        6 x 4 x 5
        1 x 2 x 3
        2 x 1 x 3
        3 x 1 x 2

        The height 60 is obtained by boxes
        [ [3, 1, 2], [1, 2, 3], [6, 4, 5], [4, 5, 6], [4, 6, 7], [32, 10, 12], [10, 12, 32] ]

Explanation 2:

Similarly, the answer for this case would be 34
"""
"""
Hint 1

Can we do something to limit our thinking of 2-D area only on two arbitrary sides of the box? There are only max 3 unique ways a box can be positioned to give unique height, width, and depth values.

If the 2-D area of 1 box is larger than the second one, can it ever come on top of the second box? What can we do with this information?


"""
"""
Solution Approach

This problem is the variation longest increasing subsequence problem.

Approach:
Let N be the initial number of boxes of we have.

    Since you can use multiple instance of the boxes, generate all the rotations of all the boxes. This will give us 3 * N boxes.
    Sort these 3*N boxes based on the base area (decreasing order of base area).

    After sorting the boxes, the problem is same as LIS with following optimal substructure property.
    maximum_Stack_height[i] = Maximum possible Stack Height with box i at top of stack
    maximum_Stack_height[i]= Max(maximum_Stack_height[i], maximum_Stack_height[j] + height[i]) where j < i and width(j) > width(i) and depth(j) > depth(i).
    If there is no such j then maximum_Stack_height[i] = height(i)
    Return the maximum value from maximum_Stack_height array.

"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return 0
            
        # dp = {}
        # for i in A:
        #     if i[0]*i[1] in dp:
        #         dp[i[0]*i[1]].append( (i[2],i[0],i[1]) )
        #     else:
        #         dp[i[0]*i[1]] = [(i[2],i[0],i[1])]
                
        #     if i[1]*i[2] in dp:
        #         dp[i[1]*i[2]].append( (i[0],i[1],i[2]) )
        #     else:
        #         dp[i[1]*i[2]] = [(i[0],i[1],i[2])]
                
        #     if i[2]*i[0] in dp:
        #         dp[i[2]*i[0]].append( (i[1],i[0],i[2]) )
        #     else:
        #         dp[i[2]*i[0]] = [(i[1],i[0],i[2])]
        
        # areas = [ i for i in dp]
        
        # areas = sorted(areas)

        
        # resDp = [ [dp[i][j][0] for j in range(len(dp[i]))] for i in areas]
        # ans = max(resDp[0])
        
        # for currBoxsIndx in range(1, len(areas)):
        #     for currBoxIndx in range( len(dp[areas[currBoxsIndx]])):
        #         temp = resDp[currBoxsIndx][currBoxIndx]
                
        #         for prevBoxsIndx in range(currBoxsIndx-1,-1,-1):
        #             for prevBoxIndx in range(len(dp[areas[prevBoxsIndx]])):
        #                 currBox = dp[ areas[currBoxsIndx] ][currBoxIndx]
        #                 prevBox = dp[ areas[prevBoxsIndx] ][prevBoxIndx]
                        
        #                 if (currBox[1] > prevBox[1] and currBox[2] > prevBox[2] )or (currBox[1] > prevBox[2] and currBox[2] > prevBox[1]):
        #                     temp = max(temp , resDp[currBoxsIndx][currBoxIndx] + resDp[prevBoxsIndx][prevBoxIndx])
                
        #         resDp[currBoxsIndx][currBoxIndx] = temp
                
        #         ans = max(ans, temp)
        
        # return ans
        
        boxes = []
        for i in A:
            boxes.append( (i[2], i[0], i[1]) )
            boxes.append( (i[0], i[1], i[2]) )
            boxes.append( (i[1], i[2], i[0]) )
        
        boxes = sorted(boxes, key= lambda x: x[1]*x[2])
        
        res = [ i[0] for i in boxes ]
        ans = res[0]
        
        # print(res)
        
        for i in range(1, len(boxes)):
            temp = res[i]
            for j in range( i-1, -1, -1):
                if (boxes[i][1] > boxes[j][1] and boxes[i][2] > boxes[j][2]) or ( boxes[i][2] > boxes[j][1] and boxes[i][1] > boxes[j][2]):
                    temp = max(temp, res[i] + res[j])
            
            res[i] = temp
        
        
        # print(boxes)
        
        return max(res)
        