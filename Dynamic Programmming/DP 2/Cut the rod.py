"""
Cut the rod


Given an integer A, and an integar vector B of size A. Cut the rod of length A into pieces such that sum of price of all pieces is maximum.
B[i] denotes price of a piece of length i.

Find and return maximum price possible after cutting the rod.


Input Format

The first argument given is integer A.
The second argument given is array B.

Output Format

Find and return maximum price possible after cutting the rod.

Constraints

1 <= A <= 10^4
1 <= B[i] <= 10^5

For Example

Input 1:
    A = 5
    B = [3, 7, 7, 10, 12]
Output 1:
    17
Explaination 1:
Rod of length 5 can be broken as :- 5 = 2 + 2 +1
answer = B[2] + B[2] + B[1] = 7 + 7 + 3 = 17 

Input 2:
    A = 6
    B = [1, 7, 9, 9 ,21, 44]
Output 2:
    44
Explaination 2:
Rod of length 6 can be broken as :- 6 = 6
answer = B[6] = 44
"""
"""
Solution Approach

Recurrence relation
DP[i] = max(B[i], DP[i - 1] + DP[1], DP[i - 2] + DP[2], DP[i - 3] + DP[3],..... and so on)

"""

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        rods = [B[0]]
        
        for size in range(2, A+1):     
            curr = B[size-1]
            rod1 = 1
            rod2 = size-rod1
            while rod1 <= rod2:
                # rod2 = size-rod1
                curr = max(curr, rods[rod1-1]+rods[rod2-1])
                
                rod1+=1
                rod2 = size-rod1
            
            rods.append(curr)
            
        return rods[-1]