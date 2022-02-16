"""
Meeting rooms


Given an array of array of integers A of size N x 2 denoting time intervals of different meetings.

Where:

A[i][0] = start time of the ith meeting.

A[i][1] = end time of the ith meeting.

find the minimum number of conference rooms required so that all meetings can be done.


Input Format

The only argument given is the matrix A.

Output Format

Return the minimum number of conference rooms required so that all meetings can be done.

Constraints

1 <= N <= 100000
0 <= A[i][0] < A[i][1] <= 2 * 10^9

For Example

Input 1:
    A = [   [0, 30]
            [5, 10]
            [15, 20] ]    
Output 1:
    2
    Meeting one can be done in conference room 1 form 0 - 30.
    Meeting two can be done in conference room 2 form 5 - 10.
    Meeting one can be done in conference room 2 form 15 - 20 as it is free in this interval.

Input 2:
   A =  [   [1, 18]
            [18, 23]
            [15, 29]
            [4, 15]
            [2, 11]
            [5, 13] ]
Output 2:
    4
    Meeting one can be done in conference room 1 from 1 - 18.
    Meeting five can be done in conference room 2 from 2 - 11.
    Meeting four can be done in conference room 3 from 4 - 15.
    Meeting six can be done in conference room 4 from 5 - 13.
    Meeting three can be done in conference room 2 from 15 - 29 as it is free in this interval.
    Meeting two can be done in conference room 4 from 18 - 23 as it is free in this interval.
"""
"""
Solution Approach

Solution 1: Use min heap to store the meeting rooms end time. If new meeting start time is greater or equal than least element, update it.
If not, open a new meeting room. Report the min heap size at the end.
Time Complexity : O(NlogN).

Solution 2: Two sorted array of start time and end time. Two pointers to iterator start array and end array. Iterate the time line, the current time active meeting is num of start minus num of end.
Since need sort, still O(nlogn) solution, but fast than solution 1.
"""
# @param A : list of list of integers
# @return an integer
def solve(self, A):

    start = []
    
    end = []
    
    for i in A:
        start.append(i[0])
        end.append(i[1])
    
    start = sorted(start)
    end = sorted(end)
    
    currActive = 0
    maxActive = 0
    ptr1 = 0
    ptr2 = 0
    
    while ptr1 < len(start) and ptr2 < len(end):
        while ptr1 <  len(start) and start[ptr1] < end[ptr2]:
            ptr1 += 1
            # print(ptr1)
        
        currActive = ptr1 - ptr2
        if currActive > maxActive:
            maxActive = currActive
        
        
        ptr2 += 1
        
    return maxActive 