"""
Max Sum Without Adjacent Elements


Problem Description

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Note: You can choose more than 2 numbers.



Problem Constraints

1 <= N <= 20000
1 <= A[i] <= 2000


Input Format

The first and the only argument of input contains a 2d matrix, A.


Output Format

Return an integer, representing the maximum possible sum.


Example Input

Input 1:

 A = [   
        [1]
        [2]    
     ]

Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]



Example Output

Output 1:

 2

Output 2:

 8



Example Explanation

Explanation 1:

 We will choose 2.

Explanation 2:

 We will choose 3 and 5.
"""
"""
Hint 1

No two adjacent elements should be taken ( Adjacent is defined by horizontally, vertically, diagonally ).

so suppose we have 2 * N list :

1 |  2  |  3  | 4
2 |  3  |  4  | 5

Now suppose we choose 2, then we can't choose the element just above it 1, 
    the element next it 3, or the element diagonally opposite. 
In other words, if we are on (x, y), then if we choose (x, y), we can't choose
(x + 1, y), (x, y + 1) and (x + 1, y + 1). 

Can you implement a brute force for this using recursion using the above fact ? 
Can you memoize the bruteforce recursive solution ? 

"""
"""
Solution Approach

Continued from Hint1:

V : 
1 |  2  |  3  | 4
2 |  3  |  4  | 5

Lets first try to reduce it into a simpler problem. 
We know that within a column, we can choose at max 1 element. 
And choosing either of those elements is going to rule out choosing anything from the previous or next column. 
This means that choosing V[0][i] or V[1][i] has identical bearing on the elements which are ruled out. 
So, instead we replace each column with a single element which is the max of V[0][i], V[1][i].

Now we have the list as : 
2 3 4 5

Here we can see that we have reduced our problem into another simpler problem.
Now we want to find maximum sum of values where no 2 values are adjacent. 
Now our recurrence relation will depend only on position i and,
 a "include_current_element" which will denote whether we picked last element or not.
  
MAX_SUM(pos, include_current_element) = 
IF include_current_element = FALSE THEN   
	max ( MAX_SUM(pos - 1, FALSE) , MAX_SUM(pos - 1, TRUE) )

ELSE
	MAX_SUM(pos - 1, FALSE) + val(pos) 

Happy Coding

"""
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def adjacent(self, A):
	    
        def util(A, curr):
            # if curr < 0:
            #     return 0
            # elif curr == 0:
            #     return max(A[0][curr], A[1][curr])
            table = [0 for i in range(curr)]
            
            table[0] = max(A[0][0], A[1][0])
            if curr==1:
                return table[-1]
            table[1] = max(table[0], max(A[0][1], A[1][1]))
            
            # print(table)
            
            for i in range(2, curr):
                table[i] = max( table[i-1], max(A[0][i], A[1][i]) + table[i-2] )
            
            # print(table)
            return table[-1]
	        
        return util(A, len(A[0]))