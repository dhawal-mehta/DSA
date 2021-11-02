"""
N integers containing only 1, 2 & 3


Problem Description

Given an integer A. Find and Return first positive A integers in ascending order containing only digits 1, 2 and 3.

NOTE: All the A integers will fit in 32 bit integer.



Problem Constraints

1 <= A <= 29500


Input Format

The only argument given is integer A.


Output Format

Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.


Example Input

Input 1:

 A = 3

Input 2:

 A = 7



Example Output

Output 1:

 [1, 2, 3]

Output 2:

 [1, 2, 3, 11, 12, 13, 21]



Example Explanation

Explanation 1:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.

Explanation 2:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
 """
 """
 Hint 1
 Can you use queue to store the integers in the ascending order?
 """
 """
Solution Appraoch

We know the initial three values will be 1, 2 and 3.

Now, the upcoming values will be by appending 1, 2 and 3 in the each given values.

We will use queue to store the elements in the ascending order.
"""
# @param A : integer
# @return a list of integers
def solve(self, A):
    queue = [1,2,3]
    ans = []
    count = A
    
    while count > 0:
        temp = queue.pop(0)
        ans.append(temp)
        queue.append(temp*10 + 1)
        queue.append(temp*10 + 2)
        queue.append(temp*10 + 3)
        count -= 1
        
    # print(ans)
    return ans
