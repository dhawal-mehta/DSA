"""
Min Jumps Array


Given an array of non-negative integers, A, of length N, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Return the minimum number of jumps required to reach the last index.

If it is not possible to reach the last index, return -1.

Input Format:

The first and the only argument contains an integer array, A.

Output Format:

Return an integer, representing the answer as described in the problem statement.

Constraints:

1 <= N <= 1e6
0 <= A[i] <= 50000

Examples:

Input 1:
    A = [2, 1, 1]

Output 1:
    1

Explanation 1:
    The shortest way to reach index 2 is
        Index 0 -> Index 2
    that requires only 1 jump.

Input 2:
    A = [2,3,1,1,4]

Output 2:
    2

Explanation 2:
    The shortest way to reach index 4 is
        Index 0 -> Index 1 -> Index 4
    that requires 2 jumps.
"""
"""
Hint 1

Dp solution is quite straight-forward here, but greedy will also work here.

Can you come up with either of the solution now?

"""
"""
Solution Approach

Greedy will work here. Think why.

With the current number of steps, try to maintain the maximum index which is reachable. When you exceed the index, you have to increase the number of steps, and at that instance you can increase the maximum index reachable accordingly.

We can mantain one variable ‘curMaxReachPos’ which stores the maximum possible distance that is possible to reach.
We can also store the maximum distance reachable till now as ‘maxReachPos’. Whenever i==maxReachPos , the maxReachPos would get updated to curMaxReachPos.
Also we can store the number of steps, whenever i==maxReachPos the number of steps would also increase. Think why.

"""
class Solution:
	# @param A : list of integers
	# @return an integer
    def jump(self, A):
        if len(A) == 1:
            return 1
            
        posReachable = A[0]
        count = 1
        
        currPos = 1
        
        while posReachable <= len(A):
            if currPos > posReachable:
                return -1
            
            if posReachable >= len(A) -1:
                return count
                
            temp = posReachable
            while currPos <= posReachable:
                temp = max(temp, currPos+A[currPos])
                currPos += 1
            
            count += 1
            posReachable = temp
        
        return count

