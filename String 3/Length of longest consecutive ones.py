"""
Length of longest consecutive ones


Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format

The only argument given is string A.

Output Format

Return the length of the longest consecutive 1’s that can be achieved.

Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.

For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
"""
"""
Hint 1

"""
"""
Solution Approach

"""
# @param A : string
# @return an integer
def solve(A):
    
    leftOnes = []
    
    count = 0
    for i in range(len(A)):
        if A[i] == '1':
            count += 1
        else:
            leftOnes.append(count)
            count = 0
            
    pos = len(leftOnes)-1
    count = 0
    print(leftOnes)
    for i in range(len(A)-1, -1, -1):
        if A[i] == '1':
            count += 1
        else:
            
            leftOnes[pos] += count
            print(count)
            pos -= 1
            count = 0
            
    print(leftOnes)
    
    return 0