"""
Evaluate Expression To True


Given an expression, A, with operands and operators (OR , AND , XOR), in how many ways can you evaluate the expression to true, by grouping in different ways?

Operands are only true and false.

Return the number of ways to evaluate the expression modulo 103 + 3.


Input Format:

The first and the only argument of input will contain a string, A.

The string A, may contain these characters:
    '|' will represent or operator 
    '&' will represent and operator
    '^' will represent xor operator
    'T' will represent true operand
    'F' will false

Output:

Return an integer, representing the number of ways to evaluate the string.

Constraints:

1 <= length(A) <= 150

Example:

Input 1:
    A = "T|F"

Output 1:
    1

Explanation 1:
    The only way to evaluate the expression is:
        => (T|F) = T 

Input 2:
    A = "T^T^F"

Output 2:
    0

Explanation 2:
    There is no way to evaluate A to a true statement.
"""
"""
Hint 1

Take an example:

T|F
The operator here is 'or'. So, we need to find the number of ways sub-expression left of `|` operator, or the sub-expression to the right of the operator, evaluates to true. 

In other words,
ways = (ways_T_left * ways_T_right) + (ways_F_left * ways_T_right) + (ways_T_left * ways_F_right)

because T | T = T
        T | F = T
        F | T = T

Can you extend the same analogy to other operators ? 

"""
"""
Solution Approach

**Continue from Hint1 **

Assume Tr(i, j) tell us the number of ways to get True from sub-expresion i to j

Fa(i, j) tell us the number of ways to get False from subexpresion i to j. 


The recurrence relation will look like the following : 

some rules => 
or operator:
T|F = T
T|T = T
F|T = T
F|F = F

and operator:
T&F = F
T&T = T
F&T = F
F&F = F

x-or operator
T^T = F
T^F = T
F^T = T
F^F = F


for Tr(i, j) :
   Loop from i to j - 1 into variable k
     IF(k == AND) :
	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Tr(k + 1, j))
     IF(k == OR) :
	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Tr(k + 1, j)) + (Tr(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j))
     If(k == XOR) :
	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j))

for Fa(i, j) :
 Loop from i to j - 1 into variable k
   IF(k == AND) :
     Fa(i, j) = Fa(i, j) + (Fa(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j)) + (Tr(i, k) * Fa(k + 1, j))
				
   IF(k == OR) :
	Fa(i, j) = Fa(i, j) + (Fa(i, k) * Fa(k + 1, j))
				
   If(k == XOR) :
	Fa(i, j) = Fa(i, j) + (Tr(i, k) * Tr(k + 1, j)) + (Fa(i, k) * Fa(k + 1, j))

then use memoziation for better time complexity

"""
class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        dpTrue = [ [0 for i in range(len(A))] for j in range(len(A)) ]
        dpFalse = [ [0 for i in range(len(A))] for j in range(len(A)) ]
        
        for i in range(0, len(A), 2):
            if A[i] == 'T':
                dpTrue[i][i] = 1
            else:
                dpFalse[i][i] = 1
        
        for sign in range(1,len(A), 2):
            if A[sign] == '|':
                if dpTrue[sign-1][sign-1] == 1 or dpTrue[sign+1][sign+1] == 1:
                    dpTrue[sign-1][sign+1] = 1
                else:
                    dpFalse[sign-1][sign+1] = 1
                
            elif A[sign] == '^':
                if (dpTrue[sign-1][sign-1] == 1 and dpFalse[sign+1][sign+1] == 1) or (dpFalse[sign-1][sign-1] == 1  and dpTrue[sign+1][sign+1] == 1):
                    dpTrue[sign-1][sign+1] = 1
                else:
                    dpFalse[sign-1][sign+1] = 1
                
            elif A[sign] == '&':
                if dpTrue[sign-1][sign-1] == 1 and dpTrue[sign+1][sign+1] == 1:
                    dpTrue[sign-1][sign+1] = 1
                else:
                    dpFalse[sign-1][sign+1] = 1
        
        # print(dpTrue)
        # print(dpFalse[:])
        # for i in range(0, len(A), 2):
        #     print(dpTrue[i])
        
        # for i in range(0, len(A), 2):
        #     print(dpFalse[i])
        
        for size in range(4, len(A), 2):
            for end in range(size, len(A), 2):
                start = end - size
                countTrue = 0
                countFalse = 0
                
                # print(start, end)
                for sign in range(start+1, end, 2):
                    # print(sign)    
                    if A[sign] == '|':
                        countTrue += dpTrue[start][sign-1]*dpFalse[sign+1][end] + dpFalse[start][sign-1]*dpTrue[sign+1][end] + dpTrue[start][sign-1]*dpTrue[sign+1][end]
                        countFalse += dpFalse[start][sign-1]*dpFalse[sign+1][end]
                        
                    elif A[sign] == '^':
                        countTrue += dpTrue[start][sign-1]*dpFalse[sign+1][end] + dpFalse[start][sign-1]*dpTrue[sign+1][end]
                        countFalse += dpTrue[start][sign-1]*dpTrue[sign+1][end] + dpFalse[start][sign-1]*dpFalse[sign+1][end]
                    
                    elif A[sign] == '&':
                        countTrue += dpTrue[start][sign-1]*dpTrue[sign+1][end]
                        countFalse += dpTrue[start][sign-1]*dpFalse[sign+1][end] + dpFalse[start][sign-1]*dpTrue[sign+1][end] + dpFalse[start][sign-1]*dpFalse[sign+1][end]
                    
                    # print("sign", sign,start,end ,countTrue, countFalse)
                    
                dpTrue[start][end] = (countTrue)%1003
                dpFalse[start][end] = (countFalse)%1003
                # print("tets", dpTrue[start][end])
            
        # for i in range(0, len(A), 2):
        #     print(dpTrue[i])
        
        # print("test", dpTrue[0][4])
        # print("-------------")
        
        # for i in range(0, len(A), 2):
        #     print(dpFalse[i])
            
        return dpTrue[0][-1]
            
                
        
        
        