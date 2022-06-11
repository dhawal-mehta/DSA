"""
Best Time to Buy and Sell Stocks I


Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.



Problem Constraints

0 <= len(A) <= 7e5

1 <= A[i] <= 1e7



Input Format

The first and the only argument is an array of integers, A.


Output Format

Return an integer, representing the maximum possible profit.


Example Input

Input 1:

A = [1, 2]

Input 2:

A = [1, 4, 5, 2, 4]



Example Output

Output 1:

1

Output 2:

4



Example Explanation

Explanation 1:

Buy the stock on day 0, and sell it on day 1.

Explanation 2:

Buy the stock on day 0, and sell it on day 2.
"""
"""
Hint 1

Basically you need to find the maximum value of A[j]-A[i] where j>i.

Now can you do this?
"""
"""
Solution Approach

If you buy your stock on day i, you’d obviously want to sell it on the day its price is maximum after that day.
So essentially at every index i, you need to find the maximum in the array in the suffix.
Now this part can be done in 2 ways :
1) Have another array which stores that information.
max[i] = max(max[i+1], A[i])

2) Start processing entries from the end maintaining a maximum till now. Constant additional space requirement.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
	    # if len(A) <= 1:
	    #     return 0
	        
	    # buy = [A[0]]
        # for i in A[1:]:
        #     if i < buy[-1]:
        #         buy.append(i)
        #     else:
        #         buy.append(buy[-1])
        
        # sell = [A[-1]]
        
        # for i in A[-2::-1]:
        #     if i > sell[-1]:
        #         sell.append(i)
        #     else:
        #         sell.append(sell[-1])
                
        # sell = sell[::-1]
        # maxl = 0
        # for i in range(len(A)):
        #     # print(sell[i], buy[i])
        #     maxl = max(maxl, sell[i] - buy[i])
        
        # # print(buy)
        # # print(sell)
        
        # return maxl

        if len(A) < 1:
            return 0

        less = A[0]
        res = 0

        for i in A[1:]:
            if i > less:
                res = max(i-less, res)
            else:
                less = i
        
        return res