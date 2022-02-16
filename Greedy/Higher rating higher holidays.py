"""
Higher rating higher holidays.


Scooby's summer vacations are about to start. Scooby and all his school friends are sitting in the class in a single line.
Every one in the class has a rating depending on their performance in InterviewBit contests. Number of holidays a child will get is dependent on the child's relative performance.

The teacher is kind and wants to give atleast one holiday to each child. If two children are sitting next to each other then the child with higher rating should always get more holidays. The teacher however wants to minimize the sum of holidays give to each child. Help the teacher in distributing holidays to children.

Constraints:

Number of children in class 1<='N'<=100000
Rating of each child 1<=R<=100000

Input: Each test case contains an integer array . This array gives the rating of the ith child.

Output: Return a single integer corresponding to the minimum sum of holidays given to children.

Example:

Input:

3 1 2 2 

Output:

4

Explanation:

Hence optimal distribution will be 1,2,1.
"""
"""
Hint 1

This problem can be solved with a greedy technique.
"""
"""
Solution Approach

This problem can be solved with a greedy technique.

We denote by the number of candies given to the child.

Let’s classify the children into four kinds, depending on the comparisons of their ratings with their neighbors.

If rating_i-1>=rating_i<=rating_i+1, we say Child is a valley.
If rating_i-1<rating_i<=rating_i+1, we say Child is a rise.
If rating_i-1>=rating_i>rating_i+1, we say Child is a fall.
If rating_i-1rating_i+1, we say Child is a peak. For the leftmost and rightmost child, assume they each have a neighbor with an infinite rating, so they can also be classified according to this scheme. (In particular, the leftmost child cannot be a rise or a peak, and the rightmost child cannot be a fall or a peak.)

Given this classification, we can intuitively distribute the candies this way:

For each valley child, give him/her 1 candy.
For each rise child, give him/her C(i-1)+1 candies.
For each fall child, give him/her C(i+1)+1 candies.
For each peak child, give him/her max(C(i-1),C(i+1))+1 candies.
Observe that this gives a valid distribution of candies. But does it give the minimum total number of candies?

Amazingly, it does! But only as long as you distribute the candies in the right order. Here’s one good order:

Distribute the candies to the valleys.
Distribute the candies to the rises from left to right.
Distribute the candies to the falls from right to left.
Distribute the candies to the peaks.
"""
# @param A : list of integers
# @return an integer
def solve(self, A):
    
    ans = [0]*len(A)
    
    ans[0] = 1
    for i in range(1, len(A) ):
        if A[i] > A[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = 1
    
    # print(ans)
    for i in range(len(A)-2, -1, -1):
        curr = 1
        if A[i] > A[i+1]:
            curr += ans[i+1]
        ans[i] = max(ans[i], curr)
    
    return sum(ans)