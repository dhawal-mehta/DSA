"""
Rod Cutting

Problem Description

There is a rod of length A lying on x-axis with its left end at x = 0 and right end at x = A. Now, there are M weak points on this rod denoted by positive integer values(all less than A) B1, B2, …, BM.

You have to cut rod at all these weak points. You can perform these cuts in any order.

After a cut, rod gets divided into two smaller sub-rods. Cost of making a cut is the length of the sub-rod in which you are making a cut.

Your aim is to minimise this cost. Return an array denoting the sequence in which you will make cuts. If two different sequences of cuts give same cost, return the lexicographically smallest.

NOTE: Sequence a1, a2 ,..., an is lexicographically smaller than b1, b2 ,..., bm, if and only if at the first i where ai and bi differ, ai < bi, or if no such i found, then n < m.



Problem Constraints

1 <= A <= 109.
1 <= M <= 100
1 <= B[i] < A


Input Format

First argument is an integer A.
Second argument is an integer array B.


Output Format

Return an array denoting denoting the sequence in which you will make cuts.


Example Input

Input 1:

 A = 6 
 B = [1, 2, 5]

Input 2:

 A = 5
 B = [1, 3]



Example Output

Output 1:

 [2, 1, 5].

Output 2:

 [3, 1]



Example Explanation

Explanation 1:

 If we make cuts in order [1, 2, 5], let us see what total cost would be.
 For first cut, the length of rod is 6. 
 For second cut, the length of sub-rod in which we are making cut is 5(since we already have made a cut at 1).
 For third cut, the length of sub-rod in which we are making cut is 4(since we already have made a cut at 2).
 So, total cost is 6 + 5 + 4.

 Cut order         | Sum of cost
(lexicographically | of each cut
 sorted)           |
___________________|_______________
[1, 2, 5]          | 6 + 5 + 4 = 15
[1, 5, 2]          | 6 + 5 + 4 = 15
[2, 1, 5]          | 6 + 2 + 4 = 12
[2, 5, 1]          | 6 + 4 + 2 = 12
[5, 1, 2]          | 6 + 5 + 4 = 15
[5, 2, 1]          | 6 + 5 + 2 = 13
 

Explanation 2:

 Minimum cost to cut is given by order [3, 1] i.e. 8."""
"""
 Hint 1

Are you convinced yet any type of greedy solution won’t work? If not, try some examples.
Let’s say from the set of cuts A1, A2, …, AN, first cut you make at is Ai.
Then, we have to make cuts from set A1, A2, …, Ai-1, whose order doesn’t depend on set of cuts Ai+1, Ai+2, …, AN.

Can you think this in terms of dynamic programming?
"""
"""
Solution Approach

We rewrite our problem as given N cut points(and you cannot make first and last cut), decide order of these cuts to minimise the cost. So, we insert 0 and N at beginning and end of vector B. Now, we have solve our new problem with respect to this new array(say A).

We define dp(i, j) as minimum cost for making cuts Ai, Ai+1, …, Aj. Note that you are not making cuts Ai and Aj, but they decide the cost for us.

For solving dp(i, j), we iterate k from i+1 to j-1, assuming that the first cut we make in this interval is Ak. The total cost required(if we make first cut at Ak) is Aj - Ai + dp(i, k) + dp(k, j).

This is our solution. We can implement this DP recursively with memoisation. Total complexity will be O(N3).
For actually building the solution, after calculating dp(i, j), we can store the index k which gave the minimum cost and then we can build the solution backwards.
"""
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, A, B):
        arr = []
        end1 = 0
        INT_MAX = float('inf')
        for end2 in B:
            arr.append(end2 - end1)
            end1 = end2
        
        arr.append(A-end1)
        
        # print(arr)
        dp = [ [ [0,[]] for i in arr] for i in arr ]
        
        B.append(A)
        
        for gap in range(1,len(arr)):
            for col in range(gap, len(arr)):
                row = col-gap
                min_ = INT_MAX
                # print('row, col',row, col)
                for i in range( 0 + row, col):
                    # print("test")b 
                    # print(row, i , i + 1, col)
                    
                    if min_ > dp[row][i][0] +  dp[i+1][col][0]:
                        minleft = [row,i]
                        minright = [i+1,col]
                        min_ = dp[row][i][0] +  dp[i+1][col][0]
                # if gap == 2:
                #     print(min_, minleft, minright)

                lengthOfRod = B[col] - (B[col-gap -1] if col-gap-1 >=0 else 0)
                dp[row][col][0] = min_ + lengthOfRod
                dp[row][col][1] = [B[ minleft[1] ]] + dp[ minleft[0] ][ minleft[1] ][1] + dp[minright[0]][minright[1]][1]
        # print(dp)
        return dp[0][-1][1]