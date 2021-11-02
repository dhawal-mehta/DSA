"""
Redundant Braces

Problem Description

Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

Chech whether A has redundant braces or not.

NOTE: A will be always a valid expression.



Problem Constraints

1 <= |A| <= 105


Input Format

The only argument given is string A.


Output Format

Return 1 if A has redundant braces, else return 0.


Example Input

Input 1:

 A = "((a+b))"

Input 2:

 A = "(a+(a+b))"



Example Output

Output 1:

 1

Output 2:

 0



Example Explanation

Explanation 1:

 ((a+b)) has redundant braces so answer will be 1.

Explanation 2:

 (a+(a+b)) doesn't have have any redundant braces so answer will be 0.
 """
 """
Hint 1

Can you maintain a stack for removing a sub expression?
"""
"""
Solution Approach

If we somehow pick out sub-expressions surrounded by ( and ), then if we are left with () as a part of the string, we know we have redundant braces.

Lets take an example:

(a+(a+b))

We keep pushing elements onto the stack till we encounter ')'. When we do encounter ')', we start popping elements till we find a matching '('. 
If the number of elements popped do not correspond to '()', we are fine and we can move forward. 
Otherwise, voila! Matching braces have been found. 

Some Extra Hints:

Try to run your code on test cases like (a*(a))  and (a) ??

Happy Coding

"""
# @param A : string
# @return an integer
def braces(A):
    stk = []
    for i in A:
        if i == '(':
            stk.append(i)
        elif i == '+' or i=='-' or i=='*' or i=='/':
            if stk:
                stk.pop()
    
    return 0 if len(stk) == 0 else 1
                