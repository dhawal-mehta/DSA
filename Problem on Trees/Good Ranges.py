"""
Good Ranges


Problem Description

Given a set S. Every number has it's own good range. It is the largest range containing only that element and no other element.
Now, given a number A, denoting the range 1 to A, and array of B queries where each element is a query having a number X in the range 1 to A. X is to be added to the set S.
For each query, the answer would be the sum of the upper and lower bound of the good ranges possible modulo 1000000007.
Finally, you need to return an array where element at i-th position represents the answer to i-th query.
NOTE : S is a set, when we add a element x which is already in S, after insertion there will be only one element with value x.



Problem Constraints
1 <= A, size of array B <= 105



Input Format
Arguments contain A, B respectivly.



Output Format
Return an array where element at i-th position represents the answer to i-th query.



Example Input
Input 1 :

A: 10
B: [2, 7, 5, 9, 6, 1, 8, 10, 3, 4]



Example Output
Output 1 :

 [11, 20, 30, 46, 58, 61, 77, 96, 102, 110]



Example Explanation
Explanation 1 :

In First 2 is added to the set and the largest range containing only 2 is [1, 10] .

Then 7 is added and the range containing only 2 becomes [1,6] and containing only 7 becomes [3, 10].

Then 5 is added and the ranges are:
    For 2 : [1,4]
    For 5 : [3,6]
    For 7 : [6,10]

Similarly for all other queries.
"""
"""
Hint 1

Try to simulate the process by having a set with 5-6 elements.
X-1, X+1 are the numbers of interest where X is some element from set. 
"""
"""
Solution Approach

Lets assume we have N elements in the set S. If we sort all the numbers then

S[i] + 1 will act as a lower bound for S[i + 1].
 
S[i] - 1 will act as a upper bound for S[i - 1].

We have to consider few number specialy.

1 will act as lower bound for first element.

'A' will act as uppoer bound for last element.

S[1] - 1 will not act as upper bound, because there is no element smaller than it. 

S[S.szie()] + 1 will not act as lower bound, because there is no element bigger than it.
"""
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        res = []
        res.append(A+1)
        last = B[0]
        first = B[0]
        
        temp = A+1
        S = set()
        S.add(B[0])
        MOD =  1000000007
        for i in range(1, len(B)):
            if B[i] not in S:
                if B[i] > last:
                    temp += last + B[i]
                    last = B[i]
                elif B[i] < first :
                    temp += first + B[i]
                    first = B[i]
                else:
                    temp += 2*B[i]
                
                S.add(B[i])
            
            # print("i",B[i], temp)
            temp = temp%MOD
            res.append(temp)
        
        # print(res)
        
        return res
            