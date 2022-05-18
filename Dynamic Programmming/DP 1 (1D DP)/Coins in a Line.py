"""
Coins in a Line


There are A coins (Assume A is even) in a line.

Two players take turns to take a coin from one of the ends of the line until there are no more coins left.

The player with the larger amount of money wins.

Assume that you go first.

Return the maximum amount of money you can win.

Input Format:

The first and the only argument of input contains an integer array, A.

Output Format:

Return an integer representing the maximum amount of money you can win.

Constraints:

1 <= length(A) <= 500
1 <= A[i] <= 1e5

Examples:

Input 1:
    A = [1, 2, 3, 4]

Output 1:
    6

Explanation 1:

    You      : Pick 4
    Opponent : Pick 3
    You      : Pick 2
    Opponent : Pick 1

    Total money with you : 4 + 2 = 6

Input 2:
    A = [5, 4, 8, 10]

Output 2:
    15

Explanation 2:

    You      : Pick 10
    Opponent : Pick 8
    You      : Pick 5
    Opponent : Pick 4

    Total money with you : 10 + 5 = 15
"""
"""
Hint 1

For each turn, we have two possibilites : We can either pick from the start or the end.

Can you find a recurrance relation by using the above fact ?
Think dynamic programming.

"""
"""
Solution Approach

So, the question is what’s the recurrence relation for this problem

Rec(player = you, start, end) = 
	    |
	max | v(end) + Rec(opposite_player, start, end - 1)  
	    |
	    | v(start) + Rec(opposite_player, start + 1, end)
	    |
Rec(player = opposite, start, end) = 
	    |
	min | Rec(you, start, end - 1)
	    |
	    | Rec(you, start + 1, end)
	    |

now can you define base cases and memorize it ?

"""
class Solution:
	# @param A : list of integers
	# @return an integer
    	
	
    def maxcoin(self, A):

        def util(A, player, start, end):
            # print(start, end , memo)
            if start > end:
                return 0
                
            if start == end - 1:
                memo[start][end] = max(A[start], A[end] )
                
                # print(start, end , memo)
                return memo[start][end]
            
            if memo[start][end] != -1:
                
                # print(start, end , memo)
                return memo[start][end]
            
            if player == 1:
                temp1 = util(A, 0, start+1, end)
                temp2 = util(A, 0, start, end-1)
                
                memo[start][end]  = max(A[start] + temp1, A[end] + temp2)
                
                # print(start, end , memo)
                return memo[start][end]
            else:
                temp1 = util(A,1,start+1,end)
                temp2 = util(A,1,start,end-1)
                
                memo[start][end] = min(temp1, temp2)
                
                # print(start, end , memo)
                return min(temp1, temp2)