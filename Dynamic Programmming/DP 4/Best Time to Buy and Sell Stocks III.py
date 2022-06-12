""" Best Time to Buy and Sell Stocks III

Say you have an array, A, for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most 2 transactions.

Return the maximum possible profit.

Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Input Format:

The first and the only argument is an integer array, A.

Output Format:

Return an integer, representing the maximum possible profit.

Constraints:

1 <= length(A) <= 7e5
1 <= A[i] <= 1e7

Examples:

Input 1:
    A = [1, 2, 1, 2]

Output 1:
    2

Explanation 1: 
    Day 0 : Buy 
    Day 1 : Sell
    Day 2 : Buy
    Day 3 : Sell

Input 2:
    A = [7, 2, 4, 8, 7]

Output 2:
    6

Explanation 2:
    Day 1 : Buy
    Day 3 : Sell
"""
"""
int 1

Think DP.

What are the essential things you need to keep in your DP states?

You will need to store maximum number of transactions you can do in any suffix/prefix of array.

"""
"""
Solution Approach

What if you construct your DP space as :
f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions

How would you fill in values in f[k, ii] and how would the DP relations look like.

"""

class Solution:
    def maxProfit(self, prices):
        min = 10**9
        maxi = 0
        maxprofit = 0
        max_before_elems = []
        for elem in prices:
            if elem < min:
                min = elem
            maxprofit = max(maxprofit,elem - min)
            max_before_elems.append(maxprofit)
        maxprofit = 0
        ans = 0
        i = len(prices)-1
        while i >= 0:
            elem = prices[i]
            if maxi < elem:
                maxi = elem
            ans = max(ans,maxi-elem+max_before_elems[i])
            i-=1

        return ans