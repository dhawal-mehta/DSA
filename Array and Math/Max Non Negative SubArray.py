"""Max Non Negative SubArray

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.


Input Format:

The first and the only argument of input contains an integer array A, of length N.

Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.

Constraints:

1 <= N <= 1e5
-INT_MAX < A[i] <= INT_MAX

Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]

Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
"""

"""
Hint 1
This problem requires a simple adhoc approach :

Just need to simulate whats stated in the problem.
Can you traverse through the array maintaining the current subset ? Note that the subset becomes invalid as soon as you encounter a negative number.

Also, note that you do not need to start again on encountering the negative number. You can start from the number next to the negative number.

"""
"""
Solution Approach

Here we go :

Loop i = 1 to Array.length :
        IF current element is positive :
                update current sum
                compare max sum with current sum
                update max sum
                update max ranges
        ELSE :
            current sum := 0
            update current ranges.
EndLoop;

return elements of max ranges

"""

def maxset(A):
    
    mx_start = -1
    mx_end = -1
    mx_sum = -1
    
    curr_start = -1
    curr_end = -1
    curr_sum = -1
    i=0
    while i < len(A):
        if A[i] <0:
            i+=1
        else:
            
            curr_start = i
            curr_end = i
            curr_sum = A[i]
            i+=1
            
            while i<len(A) and A[i] >= 0:
                curr_sum += A[i]
                curr_end += 1
                i+=1
            # print(curr_start, curr_end, curr_sum)
            if curr_sum > mx_sum or (curr_sum == mx_sum and (curr_end-curr_start)>(mx_end-mx_start)):
                mx_start = curr_start
                mx_end = curr_end
                mx_sum = curr_sum
        
            curr_start = -1
            curr_end = -1
            curr_sum = -1
            
    if mx_sum == -1:
        return []
        
    return A[mx_start:mx_end+1]