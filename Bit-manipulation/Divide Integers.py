"""Divide Integers


Problem Description

Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Also, consider if there can be overflow cases i.e output is greater than INTMAX, return INTMAX.

NOTE: INTMAX = 2^31 - 1



Problem Constraints

-231 <= A, B <= 231-1

B!= 0



Input Format

First argument is an integer A denoting the dividend.
Second argument is an integer B denoting the divisor.


Output Format

Return an integer denoting the floor value of the division.


Example Input

Input 1:

 A = 5
 B = 2

Input 2:

 A = 7
 B = 1



Example Output

Output 1:

 2

Output 2:

 7



Example Explanation

Explanation 1:

 floor(5/2) = 2
"""
# @param A : integer
# @param B : integer
# @return an integer
def divide(A, B):
    if A == -2147483648 and B == -1:
        return abs(A) -1	    
    if B==1:
        return A
    temp = 0
    q = 0
    flag = 0
    if A<0 and B>0:
        flag = 1
        
    if B<0 and A>0:
        flag = 1
    
    A = abs(A)
    B = abs(B)
    
    while A>=B:
        
        x= 0
        while A >= ( B<<1<<x ):
            # print("x+1", B<<1<<(x+1))
            x += 1
            
        A -= B<<x
        q += 1<<x



    if flag == 1:
        return -q
    return q