"""
Sort stack using another stack

Problem Description

Given a stack of integers A, sort it using another stack.

Return the array of integers after sorting the stack using another stack.


Problem Constraints

1 <= |A| <= 5000

0 <= A[i] <= 1000000000


Input Format

The only argument given is the integer array A.


Output Format

Return the array of integers after sorting the stack using another stack.


Example Input

Input 1:

 A = [5, 4, 3, 2, 1]

Input 2:

 A = [5, 17, 100, 11]



Example Output

Output 1:

 [1, 2, 3, 4, 5]

Output 2:

 [5, 11, 17, 100]



Example Explanation

Explanation 1:

 Just sort the given numbers.

Explanation 2:

 Just sort the given numbers.
"""
"""
Hint 1
Looking at the constraints, it seems like O(N^2) will pass.
Can you think of an algo now??
"""
"""
Solution Approach



    Create a temporary stack say B.

    While input stack is not empty:
    1. pop an element from input stack calls it x.
    2. while the temporary stack is not empty and top of the temporary stack is greater than x pop from the temporary stack and push it into input stack.
    3. push x in the temporary stack.

    The sorted numbers are in the temporary stack.

Worst case time complexity O(n^2).
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        tmpstack = []
        while(len(A) != 0):
            tmp = A.pop()
            while(len(tmpstack) != 0):
                val = tmpstack.pop()
                if(val > tmp):
                    A.append(val)
                else:
                    tmpstack.append(val)
                    break
            tmpstack.append(tmp)
        return tmpstack
